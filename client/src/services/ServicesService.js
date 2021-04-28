//Yes I'm going with this name
import Api from "@/services/Api";

export default {
  list() {
    return Api().get("services");
  },

  create(review) {
    return Api().post("addreview", review);
  },
};
