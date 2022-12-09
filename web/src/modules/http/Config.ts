import axios from "axios";

const standard = axios.create({
  headers: {
    post: {
      "Access-Control-Allow-Origin": "*",
    },
  },
  baseURL:
    // eslint-disable-next-line no-undef
    process.env.VUE_APP_API_URL,
  timeout: 100000,
  transformResponse: [
    function (data) {
      return data;
    },
  ],
});

export default standard;
