<template>
  <v-container>
    <v-row dense>
      <v-col v-for="member in members" :key="member.id" :cols="6">
        <v-card>
          <v-card-title>{{ member.name }}</v-card-title>
          <v-card-subtitle>{{ member.point }}pt</v-card-subtitle>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import axios from "axios";
import { defineComponent } from "vue";
import { Member } from "../interface";

export default defineComponent({
  name: "MembersList",
  data() {
    return {
      members: Array<Member>(),
    };
  },
  mounted() {
    axios.get("/api/members/").then((response) => {
      this.members = response["data"];
    });
  },
});
</script>
