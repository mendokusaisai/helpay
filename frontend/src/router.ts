import Vue from "vue";
import Router from "vue-router";
import GetPointView from "./views/GetPointView.vue";
import TestView from "./views/TestView.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "home",
      component: GetPointView,
    },
    {
      path: "/test",
      name: "test",
      component: TestView,
    },
  ],
});
