import { Slide, useScrollTrigger } from "@mui/material";

interface Props {
  window?: () => Window;
  children: React.ReactElement;
}

const HideOnScroll: React.FC<Props> = ({ window, children }) => {
  const trigger = useScrollTrigger({
    target: window ? window() : undefined,
  });

  return (
    <Slide appear={false} direction="down" in={!trigger}>
      {children}
    </Slide>
  );
};

export default HideOnScroll;
