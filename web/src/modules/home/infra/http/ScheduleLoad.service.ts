import Http from "@/modules/http/Http";
import ScheduleEntity from "../../domain/entities/Schedule.entity";

interface ScheduleDTO {
  agendamentos: any[];
}

export default class ScheduleLoadService extends Http {
  async load() {
    const response = await this.get<ScheduleDTO>("/agendamentos");

    const schedules = response.agendamentos.map(schedule => {
      const [id, cpf, date, hour] = schedule;

      const toTransform = new ScheduleEntity();

      toTransform.id = id;
      toTransform.customer.cpf = cpf;
      toTransform.date = date;
      toTransform.hour = hour;

      return toTransform;
    });

    return schedules;
  }
}
