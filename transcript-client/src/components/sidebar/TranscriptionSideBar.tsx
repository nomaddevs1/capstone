
import { Box } from "@chakra-ui/react"
import { ReactNode } from "react"

interface TranscriptionSideBarProps {
  children: ReactNode
}

const TranscriptionSideBar = ({ children }: TranscriptionSideBarProps) => {
  return (
    <Box backgroundColor={"primary.ivy.400"} overflowY="auto" height="100%" padding="4"> 
        {children}
    </Box>
  )
}

export default TranscriptionSideBar
