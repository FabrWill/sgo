import Http from "@/modules/http/Http";

export default class ScheduleService extends Http {
  async load() {
    return this.get("/agendamentos");
  }
}
