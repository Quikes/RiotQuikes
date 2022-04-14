<template>
  <v-container fluid pa-0>
    <v-row align="center" justify="center" dense>
      <v-col>
        <v-card class="ma-auto pa-4" max-width="500" max-height="800">
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
                      <h1 class="font-weight-light">Register Form</h1>
                    </div>
                  </v-col>
                  <v-col cols="12" sm="12" md="12" class="pa-0">
                    <v-text-field
                      v-model="register.email"
                      :append-icon="'mdi-email'"
                      label="email"
                      outlined
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="12" md="12" class="pa-0">
                    <v-text-field
                      v-model="register.password"
                      :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                      :rules="[rules.required, rules.min]"
                      :type="show1 ? 'text' : 'password'"
                      name="input-10-1"
                      label="password"
                      hint="At least 8 characters required."
                      counter
                      @click:append="show1 = !show1"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="12" md="12" class="pa-0">
                    <v-text-field
                      v-model="register.repeatPassword"
                      :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                      :rules="[rules.required, rules.min, rules.equal]"
                      :type="show2 ? 'text' : 'password'"
                      name="input-10-2"
                      label="confirm password"
                      hint="At least 8 characters required."
                      counter
                      @click:append="show2 = !show2"
                    ></v-text-field>
                  </v-col>
                  <v-row no-gutters style="font-size: 16px">
                    <v-col sm="6" md="8" class="pa-0">
                      <p class="font-weight-light text-right">
                        Already have an account?
                      </p>
                    </v-col>
                    <v-col sm="6" md="4" class="pa-0">
                      <p
                        class="font-weight-light text-left pl-3"
                        style="color: #86d1cd; cursor: pointer"
                        @click="backToLogin()"
                      >
                        Login
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
            >
              Create Account</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "RegisterForm",
  data() {
    return {
      register: {
        email: "",
        password: "",
        repeatPassword: "",
      },
      show1: false,
      show2: false,
      rules: {
        required: (value) => !!value || "Wymagane.",
        min: (v) => v.length >= 8 || "Conajmniej 8 znaków",
        equal: (text) =>
          text === this.register.password || "Hasła muszą być identyczne",
      },
    };
  },
  methods: {
    backToLogin() {
      this.$router.push("/login");
    },
  },
};
</script>

<style></style>
