export default class ServiceEntity {
  id = 0;
  name = "";
  value = 0;

  static build(params: ServiceEntity) {
    const service = new ServiceEntity();

    service.id = params.id;
    service.name = params.name;
    service.value = params.value;

    return service;
  }
}
