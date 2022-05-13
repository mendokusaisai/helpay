import { createApp } from "vue";
import App from "./App.vue";
import { worker } from "./mocks/browser";
import "./registerServiceWorker";
import router from "./router";

if (process.env.NODE_ENV === "development") {
  worker.start();
}

createApp(App).use(router).mount("#app");
