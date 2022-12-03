import { Grow } from "@mui/material";
import { TransitionProps } from "@mui/material/transitions";
import React from "react";

export const GrowTransition = React.forwardRef(function Transition(
    props: TransitionProps & {
      children: React.ReactElement;
    },
    ref: React.Ref<unknown>,
  ) {
    return <Grow ref={ref} {...props} />;
  });
  