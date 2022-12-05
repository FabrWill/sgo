import React, { useState } from "react";
import Calendar from "react-calendar";
import ScheduleDialog from "../components/schedule_dialog/ScheduleDialog";
import {
  ScheduleDialogStore,
  useScheduleStore,
} from "../components/schedule_dialog/ScheduleDialog.store";
import "./Schedule.page.scss";

interface Props {}

const SchedulePage: React.FC<Props> = ({}) => {
  const [value, onChange] = useState(new Date());

  const scheduleDialog = useScheduleStore();

  return (
    <div>
      <Calendar
        onChange={onChange}
        value={value}
        onClickDay={() => scheduleDialog.open()}
      />

      <ScheduleDialog store={scheduleDialog} />
    </div>
  );
};

export default SchedulePage;
