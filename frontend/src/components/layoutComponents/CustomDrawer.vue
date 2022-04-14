<template>
  <div>
    <v-card>
      <v-layout>
        <v-navigation-drawer
          theme="dark"
          image="https://cdn.vuetifyjs.com/images/backgrounds/bg-2.jpg"
          width="100%"
          permanent
        >
          <v-list nav color="transparent">
            <v-list-item
              prepend-icon="mdi-email"
              title="Inbox"
              value="inbox"
            ></v-list-item>
            <v-list-item
              prepend-icon="mdi-account-supervisor-circle"
              title="Supervisors"
              value="supervisors"
            ></v-list-item>
            <v-list-item
              prepend-icon="mdi-clock-start"
              title="Clock-in"
              value="clockin"
            ></v-list-item>
          </v-list>
        </v-navigation-drawer>
        <v-main style="height: 100vh"></v-main>
      </v-layout>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "CustomDrawer",
  methods: {
    goTo(link) {
      this.$router.push(link);
    },
  },
};
</script>
