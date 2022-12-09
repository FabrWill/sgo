import Http from "@/modules/http/Http";

export default class ScheduleService extends Http {
    load () {
        this.get("/");
    }
}
