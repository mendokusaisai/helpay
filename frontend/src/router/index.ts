import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import CardsView from "../views/CardsView.vue";
import HelpayView from "../views/HelpayView.vue";
import HomeView from "../views/HomeView.vue";
import MembersView from "../views/MembersView.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/helpay",
    name: "helpay",
    component: HelpayView,
  },
  {
    path: "/cards",
    name: "cards",
    component: CardsView,
  },
  {
    path: "/members",
    name: "members",
    component: MembersView,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
