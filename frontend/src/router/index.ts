import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import CardsView from "../views/CardsView.vue";
import HelpayView from "../views/HelpayView.vue";
import MembersView from "../views/MembersView.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
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
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
