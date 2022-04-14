<template>
  <div id="deflayout">
    <v-navigation-drawer expand-on-hover rail style="transform: translateX(0%)">
      <v-list>
        <v-list-item
          :prepend-avatar="require('./assets/league_logo_big.png')"
          title="QuikeSoft"
          subtitle="Riot Api Testing"
        ></v-list-item>
      </v-list>

      <v-divider></v-divider>

      <v-list density="compact" nav>
        <v-list-item
          v-for="item in items"
          :key="item.title"
          :prepend-icon="item.icon"
          :title="item.title"
          :value="item.title"
          @click="goTo(item.link)"
          class="text-grey-darken-2"
        >
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <div id="content" class="mb-10"><slot /></div>
    <custom-footer />
  </div>
</template>

<script>
import auth from "@/auth";
import { mapState, mapActions } from "vuex";

import CustomFooter from "./components/layoutComponents/CustomFooter.vue";

export default {
  name: "DefLayout",
  data() {
    return {
      items: [
        // {
        //   title: "Pobierz szablon",
        //   icon: "mdi-download-circle-outline",
        //   link: "/import",
        // },
        // {
        //   title: "Import danych",
        //   icon: "mdi-application-import",
        //   link: "/prof",
        // },
        // {
        //   title: "Weryfikacja",
        //   icon: "mdi-pencil-box-multiple-outline",
        //   link: "/verify",
        // },
        { title: "Profile", icon: "mdi-account", link: "/profile" },
        { title: "Logout", icon: "mdi-logout", link: null },
      ],
      right: null,
    };
  },
  methods: {
    ...mapActions("currentUser", ["getCurrentUser"]),
    goTo(link) {
      if (!link) {
        auth.logout();
      } else {
        this.$router.push({ path: link });
      }
    },
  },
  computed: {
    ...mapState({
      currentUser: (state) => state.currentUser.currentUser,
      confirm: (state) => state.currentUser.isConfirm,
    }),
  },
  created() {
    if (auth.checkAuth()) this.getCurrentUser();
  },
  components: { CustomFooter },
};
</script>
<style></style>
