<template>
  <div class="menbers_list">
    <button v-if="isEdit">追加</button>
    <ul>
      <li v-for="member in members" v-bind:key="member.name">
        <div>
          <p>{{ member.name }}</p>
          <p>{{ member.point }}point</p>
          <button v-if="isEdit">削除</button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import axios from "axios";
import { defineComponent } from "vue";
import { Member } from "../interface";

export default defineComponent({
  name: "CardsList",
  props: {
    isEdit: {
      type: Boolean,
      default: false,
    },
  },
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
