<template>
  <v-container class="helpay">
    <MembersList />
    <v-divider></v-divider>
    <TaskList />
  </v-container>
</template>

<script lang="ts">
import MembersList from "@/components/MembersList.vue";
import TaskList from "@/components/TaskList.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "HelpayView",
  components: {
    MembersList,
    TaskList,
  },
});
</script>
