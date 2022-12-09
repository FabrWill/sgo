import Http from "@/modules/http/Http";
import ScheduleEntity from "../../domain/entities/Schedule.entity";

export default class ScheduleSaveService extends Http {
  async save(schedule: ScheduleEntity) {
    return this.post("/agendamento", {
      data: schedule.date,
      hora: schedule.hour,
      cpf: schedule.customer.cpf,
    });
  }
}
