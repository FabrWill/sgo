import { observer } from "mobx-react-lite";
import { ScheduleRegisterDialogStore } from "./ScheduleRegisterDialog.store";
import { Dialog, DialogTitle, Divider, DialogContent } from "@mui/material";
import { GrowTransition } from "../../../../../shared/navigation/GrodAnimation";

interface Props {
    store: ScheduleRegisterDialogStore;
}

const ScheduleRegisterDialog: React.FC<Props> = observer(({ store }) => {
  return <>
    <Dialog open={store.isOpen} onClose={() => store.close()} TransitionComponent={GrowTransition} maxWidth="lg" fullWidth>
        
    <DialogTitle sx={{ fontFamily: "Raleway" }}>Agendamentos</DialogTitle>

    <DialogContent>

    </DialogContent>
    </Dialog>
  </>;
});

export default ScheduleRegisterDialog;