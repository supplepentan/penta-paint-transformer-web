<template>
  <div class="container home">
    <div class="row">
      <Viewer msg="Penta Paint Transformer" seen1="true" />
    </div>
    <br/>
    <div class="row">
      <div v-show="seen1" class="col-12">
        <p><input type="file" v-on:change="fileSelected" /></p>
      </div>
      <div v-show="seen2" class="col-12">
        <button v-on:click="fileUpload">変換開始</button>
      </div>
      <div v-show="seen3" class="col-12"><p>画像変換中</p></div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Viewer from "@/components/Viewer.vue"; // @ is an alias to /src
import axios from "axios";

export default defineComponent({
  name: "Home",
  components: {
    Viewer,
  },
  data: function () {
    return {
      fileInfo: "",
      // ダウンロード URL (Blob)
      downloadUrl: null,
      // ファイル名
      fileName: "no01",
      requestBody: "",
      seen0: true,
      seen1: true,
      seen2: false,
      seen3: false,
      picked: "papapa",
      showUserImage: "",
    };
  },
  methods: {
    fileSelected(event: any) {
      this.fileInfo = event.target.files[0];
      console.log("kokokokoo");
      console.log(this.picked);
      this.seen2 = true;
    },
    async fileUpload(): Promise<void> {
      const formData: any = new FormData();
      formData.append("file", this.fileInfo);
      console.log(formData);
      console.log(...formData.entries());
      this.seen0 = false;
      this.seen1 = false;
      this.seen2 = false;
      this.seen3 = true;
      axios.post("http://127.0.0.1:8000/upload", formData).then((response) => {
        this.seen0 = true;
        this.seen1 = true;
        this.seen3 = false;
      });
    },
  },
});
</script>
