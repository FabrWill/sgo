import Service from "../../../services/domain/entities/Service.entity";
import EScheduleStatus from "../enums/ScheduleStatus.enum";

export default class Schedule {
    id: number = 0;
    cpf?: string;
    data?: string;
    hora?: string;
    services: Service[] = [];
    status?: string = EScheduleStatus.WAITING;
}