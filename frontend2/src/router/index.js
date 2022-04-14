import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import TierList from "@/components/TierList";
import LoginView from "@/components/LoginView";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/tiers",
    name: "tiers",
    component: TierList,
  },
  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
  // {
  //   path: "/about",
  //   name: "about",
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () =>
  //     import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  // },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to) => {
  //store.dispatch('cancel/CANCEL_PENDING_REQUESTS')
  if (to.path == "/login") {
    // Not logged in? You get booted to /login
    window.location.href = "/api/v1/accounts/login";
    console.log("if" + to.path);
  }
});
export default router;
