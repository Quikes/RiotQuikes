import { createRouter, createWebHistory } from "vue-router";
import Login from "@/components/authorizationModule/Login.vue";
import Register from "@/components/authorizationModule/Register.vue";
import LandingPage from "../views/LandingPage.vue";
import ImportView from "../views/ImportView.vue";
import ProfileView from "../views/ProfileView";
import PrivacyPolicy from "../components/informations/PrivacyPolicy";
import TermsServices from "../components/informations/TermsServices";
import auth from "@/auth";
import store from "@/store";

const routes = [
  {
    path: "/",
    name: "LandingPage",
    component: LandingPage,
    meta: { layout: "DefLayout" },
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
    meta: { layout: "LoginLayout", title: "- loginpage" },
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
    meta: { layout: "LoginLayout", title: "- register" },
  },
  {
    path: "/import",
    name: "Import",
    component: ImportView,
    meta: { title: "- import" },
  },
  {
    path: "/profile",
    name: "Profile",
    component: ProfileView,
    meta: { title: "- profile", layout: "DefLayout" },
  },
  {
    path: "/polityka",
    name: "PrivacyPolicy",
    component: PrivacyPolicy,
    meta: { layout: "MainLayout", title: "- polityka prywatności" },
  },
  {
    path: "/regulamin",
    name: "TermsServices",
    component: TermsServices,
    meta: { layout: "MainLayout", title: "- regulamin serwisu" },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  scrollBehavior() {
    return { top: 0 };
  },
});

router.beforeEach((to, from, next) => {
  let confirmProfile = store.getters["currentUser/isConfirm"];
  auth.checkAuth();
  const unauthCanAccess = [
    "Login",
    "Register",
    // "LandingPage",
    "PrivacyPolicy",
    "TermsServices",
  ];
  if (!unauthCanAccess.includes(to.name) && !auth.user.authenticated) {
    next({ name: "Login" });
  } else if (
    !confirmProfile &&
    auth.user.authenticated &&
    !unauthCanAccess.includes(to.name) &&
    to.name != "Profile" &&
    from.name === "Login"
  ) {
    next({ name: "Profile" });
  } else next();
});

const DEFAULT_TITLE = "QuikeSoft";
router.afterEach((to) => {
  document.title = DEFAULT_TITLE + (to.meta.title ? to.meta.title : "");
});

export default router;
