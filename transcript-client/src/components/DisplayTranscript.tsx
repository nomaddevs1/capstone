import { Box, Text, Button } from "@chakra-ui/react";
import { useContext } from 'react';
import { TranscriptionContext } from 'src/context/TranscriptionContext';

function DisplayTranscript (){
    const transcription: any = useContext(TranscriptionContext);
    const displayText = () => {
        if (transcription){
            const arr:Array<JSX.Element> = [];
            for (let i = 0; i < transcription.transcriptionData.length; i++){
              //@ts-ignore
                arr.push(<Text key={i} mb={4}>{transcription.transcriptionData[i].text}</Text>);
            }
            return arr;
        }
    }

    return (
        <Box height="100vh">
            <Box pt={20} pl={40} pr={40} height="80vh" pos="relative">
                <Box overflowY="auto" height="100%" bg="primary.moss.100" p={6} textAlign="left">
                    {displayText()}
                </Box>
            </Box>
            <Button mt={10}>Customize Transcript</Button>
        </Box>
    );
}

export default DisplayTranscript;
