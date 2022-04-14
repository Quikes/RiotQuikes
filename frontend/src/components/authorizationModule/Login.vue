<template>
  <v-container fluid pa-0>
    <v-row align="center" justify="center" dense>
      <v-col>
        <v-card class="ma-auto pa-4" max-width="500" max-height="650">
          <v-card-title class="align-center justify-center">
            <v-img
              :src="require('../../assets/league_logo_big.png')"
              class="my-3"
              contain
              height="250"
            />
          </v-card-title>
          <v-card-text>
            <v-form>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="12" md="12" class="pb-10">
                    <div style="text-align: center">
                      <h1 class="font-weight-light">Login</h1>
                    </div>
                  </v-col>
                  <v-col cols="12" sm="12" md="12" class="pa-0">
                    <v-text-field
                      label="login"
                      outlined
                      v-model="credentials.login"
                      :append-icon="'mdi-email'"
                      v-on:keydown.enter="logIn()"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="12" md="12" class="pa-0">
                    <v-text-field
                      v-model="credentials.password"
                      :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                      :rules="[rules.required, rules.min]"
                      :type="show1 ? 'text' : 'password'"
                      name="input-10-1"
                      label="password"
                      hint="At least 8 characters required."
                      counter
                      @click:append="show1 = !show1"
                      v-on:keydown.enter="logIn()"
                    ></v-text-field>
                    <!-- <v-text-field
                      label="Hasło"
                      placeholder=""
                      filled
                      v-model="credentials.password"
                    ></v-text-field> -->
                  </v-col>
                  <v-row no-gutters style="font-size: 16px">
                    <v-col sm="3" md="6" class="pa-0">
                      <p class="font-weight-light text-right">No account?</p>
                    </v-col>
                    <v-col sm="3" md="6" class="pa-0">
                      <p
                        class="font-weight-light text-left pl-3"
                        style="color: #86d1cd; cursor: pointer"
                        @click="goToRegister()"
                      >
                        Register
                      </p>
                    </v-col>
                  </v-row>
                </v-row>
              </v-container>
            </v-form>
          </v-card-text>
          <v-card-actions class="justify-center">
            <v-btn
              rounded="pill"
              color="white"
              style="width: 80%; background: #17728d"
              @click="logIn()"
            >
              login</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import auth from "../../auth";
export default {
  name: "AuthorizationForm",
  data() {
    return {
      credentials: {
        login: "",
        password: "",
      },
      show1: false,
      rules: {
        required: (value) => !!value || "Wymagane.",
        min: (v) => v.length >= 8 || "At least 8 characters required.",
      },
    };
  },
  methods: {
    goToRegister() {
      this.$router.push("/register");
    },
    logIn() {
      let credentials = {
        username: this.credentials.login,
        password: this.credentials.password,
      };
      auth.login(this, credentials);
    },
  },
};
</script>

<style></style>
