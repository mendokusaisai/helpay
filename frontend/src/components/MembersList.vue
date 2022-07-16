<template>
  <v-container>
    <p>{{ selections }}</p>
    <v-row dense>
      <v-col v-for="member in members" :key="member.id" :cols="6">
        <v-card
          :color="selections.includes(member.id) ? 'primary' : undefined"
          :dark="selections.includes(member.id)"
          class="mx-auto"
          rounded="xl"
          @click="changeSelection(member.id)"
        >
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
      active: false,
      selections: Array<number>(),
    };
  },
  mounted() {
    axios.get("/api/members/").then((response) => {
      this.members = response["data"];
    });
  },
  methods: {
    changeSelection: function (memberId: number) {
      if (this.selections.includes(memberId)) {
        this.selections.splice(this.selections.indexOf(memberId), 1);
      } else {
        this.selections.push(memberId);
      }
    },
  },
});
</script>
