<template>
  <v-app>
    <v-app-bar app>
      <v-app-bar-title>Helpay</v-app-bar-title>
      <v-spacer />
      <v-toolbar-items>
        <v-tabs align-with-title>
          <v-tab flat to="/">helpay</v-tab>
          <v-tab flat to="/cards">cards</v-tab>
          <v-tab flat to="/members">members</v-tab>
          <v-tab flat to="/test">test</v-tab>
        </v-tabs>
      </v-toolbar-items>
    </v-app-bar>
    <v-main>
      <v-content>
        <router-view />
      </v-content>
    </v-main>
  </v-app>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "App",

  data() {
    return {
      //
    };
  },
});
</script>
