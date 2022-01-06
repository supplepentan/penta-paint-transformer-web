<template>
  <div class="container">
    <div class="container hello">
      <h1>{{ msg }}</h1>
      <div class="container">
        <div class="row">
          <div class="col-1"></div>
          <div class="col-5">
            <img src="@/../../input/input.jpg" class="img-fluid" alt="" />
          </div>
          <div class="col-5">
            <img src="@/../../output/input.jpg" class="img-fluid" alt="" />
          </div>
          <div class="col-1"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "Viewer",
  props: {
    msg: String,
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
