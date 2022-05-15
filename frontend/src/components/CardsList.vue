<template>
  <!-- カード一覧 -->
  <div class="cards_list">
    <!-- 追加ボタン -->
    <button v-on:click="addCard">追加</button>
    <button v-on:click="saveCards">保存?</button>
    <ul>
      <li v-for="card in cards" v-bind:key="card.id">
        <!--カード情報-->
        <div class="card">
          <input name="name" type="text" v-model="card.name" />
          <input name="point" type="text" v-model="card.point" />
          <!-- 対象設定をここで行う -->
          <div v-for="(member, key) in members" v-bind:key="key">
            <input
              :id="'card' + card.id + 'member' + key"
              type="checkbox"
              :value="member"
              v-model="card.targets"
            />
            <label :for="'card' + card.id + 'member' + key">{{
              member.name
            }}</label>
          </div>
          <!-- 削除ボタン -->
          <button v-on:click="deleteCard(card.id)">削除</button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
export interface CardPayload {
  id: number;
  name: string;
  point: number;
  targets: Array<number>;
}

import axios from "axios";
import { defineComponent } from "vue";
import { Card, Member } from "../interface";

export default defineComponent({
  name: "CardsList",
  props: {
    msg: String,
  },
  data() {
    return {
      cards: Array<Card>(),
      members: Array<Member>(),
    };
  },
  mounted() {
    axios.get("/api/cards/").then((response) => {
      this.cards = response["data"];
      console.log(this.cards);
    });

    axios.get("/api/members/").then((response) => {
      this.members = response["data"];
    });
    console.log(this.cards);
  },
  methods: {
    addCard: function () {
      axios.get("api/cards/new/").then((response) => {
        this.cards.push(response["data"]);
      });
      axios.get("/api/cards/").then((response) => {
        this.cards = response["data"];
        console.log(this.cards);
      });
    },
    deleteCard: function (target_id: number) {
      console.log(this.cards);
      console.log(target_id);
      const data = { id: target_id.toFixed() };
      axios.post("api/cards/delete/", data).then((response) => {
        console.log(response.data);
      });
      axios.get("/api/cards/").then((response) => {
        this.cards = response["data"];
        console.log(this.cards);
      });
    },
    saveCards: function () {
      var payload: CardPayload[] = [];
      this.cards.forEach((element: Card) => {
        var _target: number[] = [];
        element["targets"].forEach((member: Member) => {
          _target.push(member["id"]);
        });
        payload.push({
          id: element["id"],
          name: element["name"],
          point: element["point"],
          targets: _target,
        });
      });
      axios.post("api/cards/save/", payload).then((response) => {
        console.log(response.data);
      });
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
</style>
