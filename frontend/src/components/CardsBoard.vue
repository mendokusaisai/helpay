<template>
  <div class="cards_board">
    <ul>
      <li v-for="card in cards" v-bind:key="card.name">
        <!--カード情報-->
        <div class="card">
          <p>{{ card.name }}</p>
          <p>{{ card.point }}point</p>
          <!-- ポイント付与ボタン -->
          <div v-for="(member, key) in card.targets" v-bind:key="key">
            <button>{{ member.name }}</button>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import axios from "axios";
import { defineComponent } from "vue";
import { Card } from "../interface";

export default defineComponent({
  name: "CardsBoard",
  props: {},
  data() {
    return {
      cards: Array<Card>(),
    };
  },
  mounted() {
    axios.get("/api/cards/").then((response) => {
      this.cards = response["data"];
    });
  },
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
