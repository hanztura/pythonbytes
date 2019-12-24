Vue.use(window.vuelidate.default)
var validationMixin = window.vuelidate.validationMixin

var required = window.validators.required

vueFormApp = new Vue({
  components: {
    VueRecaptcha
  },

  name: 'Simple Subscriber Plugin',

  el: '#form--simple_subscriber_plugin',

  delimiters: ['[[', ']]'],

  data: () => {
    return {
      emailAddress: '',
      disableSubmit: false,
      recaptchaResponse: '',
      sent: false,
      submitUrl: '',

      errorMessage: {
        required: 'Field is required.',
      },
      widgetId: 0,
    }
  },
  methods: {
    submitForm(e) {
      this.disableSubmit = true;
      this.$v.$touch();

      if (!this.$v.$invalid) {
        // valid form
        let _this = this;
        data = {
          'email_address': this.emailAddress,
          'captcha': this.recaptchaResponse,
        }

        // set url from form action attribute
        this.submitUrl = e.target.getAttribute('action')

        axios
          .post(this.submitUrl, data)
          .then(response => {
            console.log(response);
            this.resetCaptcha();
            this.$refs.formSubscribe.reset();
            this.sent = true;
            this.$refs.checkIcon.classList.add('animated', 'fadeInUp');
            setTimeout(() => {
              _this.sent = false;
            }, 60000);
          })
          .catch(error => {
            console.log(error);
          })
          .finally(() => {
            _this.disableSubmit = false;
          })
      } else {
        // not valid
        this.disableSubmit = false;
      }
    },
    setRecaptchaResponse(recaptchaToken) {
      this.$set(this.$v.recaptchaResponse, '$model', recaptchaToken);
    },

    onCaptchaExpired: function () {
      this.resetCaptcha();
    }, 

    onCaptchaVerified: function (recaptchaToken) {
      this.setRecaptchaResponse(recaptchaToken);
    },

    resetCaptcha: function () {
      this.$refs.recaptcha.reset();
      this.$set(this.$v.recaptchaResponse, '$model', '');
    },
  },

  validations: {
    emailAddress: {
      required,
    },
    recaptchaResponse: {
      required,
    },
  },

  mounted () {}
});