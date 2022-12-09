import Http from "@/modules/http/Http";

export default class CustomerService extends Http {
  async load() {
    return this.get("/clientes");
  }
}
