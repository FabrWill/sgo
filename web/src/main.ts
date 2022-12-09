import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import VuetifyMask from "vuetify-mask";
import vuetify from "./plugins/vuetify";

Vue.config.productionTip = false;

Vue.use(VuetifyMask as any);

new Vue({
  vuetify,
  router,
  render: h => h(App),
}).$mount("#app");
