import ScheduleEntity from "./Schedule.entity";

export default class EventEntity {
  static scheduleToEvent(schedules: ScheduleEntity[]) {
    return schedules.map(schedule => {
      return {
        start: new Date(`${schedule.date}T${schedule.hour}:00`),
        end: new Date(`${schedule.date}T${schedule.hour}:00`),
        name: `${schedule.customer.cpf}`,
      };
    });
  }
}
