let vueSimpleContactForm = new Vue({
  components: {
    VueRecaptcha
  },

  data: () =>{
    return {
      disableSubmit: false,
      recaptchaResponse: '',
      sent: false,
    }
  },

  methods: {
    submitForm(e) {
      this.disableSubmit = true;

      if (this.recaptchaResponse != '') {
        // valid form
        let _this = this;
        data = {
          'name': this.$refs.name.value,
          'email_address': this.$refs.emailAddress.value,
          'message': this.$refs.message.value,
          'captcha': this.recaptchaResponse,
        }

        // set url from form action attribute
        let submitUrl = e.target.getAttribute('action')

        axios
          .post(submitUrl, data)
          .then(response => {
            console.log(response);
            _this.sent = true;
            _this.resetCaptcha();
            e.target.reset();
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
      this.recaptchaResponse = recaptchaToken;
    },

    onCaptchaExpired: function () {
      this.resetCaptcha();
    }, 

    onCaptchaVerified: function (recaptchaToken) {
      this.setRecaptchaResponse(recaptchaToken);
    },

    resetCaptcha: function () {
      this.$refs.recaptcha.reset();
      this.recaptchaResponse = '';
    },
  },

  el: '#form--simple-contact-form',
  name: 'SimpleContactForm',
  delimiters: ['[[', ']]'],
});