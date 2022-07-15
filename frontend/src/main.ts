import Vue from "vue";
import App from "./App.vue";
import { worker } from "./mocks/browser";
import vuetify from "./plugins/vuetify";
import router from "./router";

if (process.env.NODE_ENV === "development") {
  worker.start();
}
Vue.config.productionTip = false;

new Vue({
  router,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
