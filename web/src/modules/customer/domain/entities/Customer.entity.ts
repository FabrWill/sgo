import ECivilStatus from "../../../home/domain/enums/CivilStatus.enum";
import EGender from "../../../home/domain/enums/Gender.enum";

export default class CustomerEntity {
  id = 0;
  name = "";
  birthdate = "";
  cpf = "";
  civil_status = ECivilStatus.SOLTEIRO;
  gender = EGender.MALE;
}
