<template>
  <div class="cards_board">
    <div>
      <button v-on:click="save">保存</button>
    </div>
    <ul>
      <li v-for="member in members" v-bind:key="member.id">
        <p>{{ member.name }}</p>
        <p>{{ member.point }}point</p>
      </li>
    </ul>

    <ul>
      <li v-for="card in cards" v-bind:key="card.name">
        <!--カード情報-->
        <div class="card">
          <p>{{ card.name }}</p>
          <p>{{ card.point }}point</p>
          <!-- ポイント付与ボタン -->
          <div v-for="(member, key) in card.targets" v-bind:key="key">
            <button
              :id="card.id + 'to' + member.id"
              v-on:click="addPoint(member.id, card.id, card.point)"
              class=""
            >
              {{ member.name }}
            </button>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import axios from "axios";
import { defineComponent } from "vue";
import { Card, Member } from "../interface";

export default defineComponent({
  name: "CardsBoard",
  data() {
    return {
      cards: Array<Card>(),
      members: Array<Member>(),
    };
  },
  mounted() {
    axios.get("/api/cards/").then((response) => {
      this.cards = response["data"];
    });
    axios.get("/api/members/").then((response) => {
      this.members = response["data"];
    });
  },
  methods: {
    addPoint: function (memberId: number, cardId: number, cardPoint: number) {
      const button = document.getElementById(
        cardId.toString() + "to" + memberId.toString()
      );
      if (button) {
        if (button.getAttribute("class") == "pushed") {
          button.setAttribute("class", "");
          for (var m1 of this.members) {
            if (m1.id == memberId) {
              m1.point -= cardPoint;
            }
          }
        } else {
          button.setAttribute("class", "pushed");
          for (var m2 of this.members) {
            if (m2.id == memberId) {
              m2.point += cardPoint;
            }
          }
        }
      }
    },
    save: function () {
      axios.post("api/members/save/", this.members).then((response) => {
        console.log(response.data);
      });
      var buttons = document.getElementsByClassName("pushed");
      var elements = Array.from(buttons);
      elements.forEach((x) => x.setAttribute("class", ""));
    },
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
button.pushed {
  background-color: #9191e8;
}
</style>
