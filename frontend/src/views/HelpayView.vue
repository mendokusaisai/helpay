<template>
  <div class="helpay">
    <h1>This is an helpay page</h1>
    <MembersList v-bind:is-edit="false" />
    <CardsBoard msg="card1" />
  </div>
</template>

<script lang="ts">
import CardsBoard from "@/components/CardsBoard.vue";
import MembersList from "@/components/MembersList.vue"; // @ is an alias to /src
import { defineComponent } from "vue";

export default defineComponent({
  name: "HelpayView",
  components: {
    MembersList,
    CardsBoard,
  },
});
</script>
