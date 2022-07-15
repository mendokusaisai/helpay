<template>
  <div class="members">
    <MembersList />
  </div>
</template>

<script lang="ts">
import MembersList from "@/components/MembersList.vue"; // @ is an alias to /src
import { defineComponent } from "vue";

export default defineComponent({
  name: "MembersView",
  components: {
    MembersList,
  },
});
</script>
