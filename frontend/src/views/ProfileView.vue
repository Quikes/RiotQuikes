<template>
  <v-card elevation="1" class="ma-16" max-width="450">
    <v-row>
      <v-col sm="4">
        <v-card-title>{{ this.currentUser.riot_name }} </v-card-title>
        <v-card-text> : {{ this.currentUser.riot_name }} Test</v-card-text>
        <input
          class="input_text"
          v-model="new_summoner_name"
          placeholder="edit me"
          color="rgb(255,255,255)"
        />
      </v-col>
      <v-col>test</v-col>
    </v-row>
    <v-card-actions>
      <v-btn
        @click="
          this.changeCurrentUserSummonerName({
            id: this.currentUser.id,
            riot_name: this.new_summoner_name,
          })
        "
        >test
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { mapState, mapActions } from "vuex";
import auth from "@/auth";

export default {
  name: "ProfileView",
  data() {
    return {
      new_summoner_name: "",
    };
  },

  methods: {
    ...mapActions("currentUser", [
      "getCurrentUser",
      "changeCurrentUserSummonerName",
    ]),
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
};
</script>

<style lang="scss" scoped>
.input_text {
  color: rgb(5, 0, 54);
  background-color: rgba(130, 187, 193, 0.653);
}
</style>
