import Http from "@/modules/http/Http";
import ServiceEntity from "../../domain/entities/Services.entity";

interface ServiceLoadDTO {
  servicos: any[];
}

export default class ServiceLoadService extends Http {
  async load(): Promise<ServiceEntity[]> {
    const response = await this.get<ServiceLoadDTO>("/servicos");

    console.log(response);

    return [];
  }
}
