import { createContext, useContext, useState } from "react";
import {
  TranscriptionContextType,
  TranscriptionData,
} from "src/types/transcriptionDataTypes";

interface ExtendedTranscriptionContextType extends TranscriptionContextType {
  audioFile: File | null;
  setAudioFile: React.Dispatch<React.SetStateAction<File | null>>;
}

const defaultState: ExtendedTranscriptionContextType = {
  transcriptionData: null,
  setTranscriptionData: () => null,
  fontSize: "16px",
  setFontSize: () => {},
  fontColor: "#000000",
  setFontColor: () => {},
  fontStyle: "Arial",
  setFontStyle: () => {},
  highlightColor: "",
  setHighlightColor: () => {},
  lineHeight: 1.5,
  setLineHeight: () => {},
  wordSpacing: "normal",
  setWordSpacing: () => {},
  isBold: false,
  setIsBold: () => {},
  isItalic: false,
  setIsItalic: () => {},
  isUnderline: false,
  setIsUnderline: () => {},
  audioFile: null,
  setAudioFile: () => null,
  resetStyles: () => {},
};

export const TranscriptionContext =
  createContext<ExtendedTranscriptionContextType>(defaultState);

export const TranscriptionProvider = ({ children }: any) => {
  const [transcriptionData, setTranscriptionData] = useState<
    TranscriptionData[] | null
  >(null);
  const [fontSize, setFontSize] = useState<string>("16px");
  const [fontColor, setFontColor] = useState<string>("#000000");
  const [highlightColor, setHighlightColor] = useState<string>("");
  const [lineHeight, setLineHeight] = useState<number>(1.5);
  const [fontStyle, setFontStyle] = useState<string>("Arial");
  const [wordSpacing, setWordSpacing] = useState<string>("normal");
  const [isBold, setIsBold] = useState<boolean>(false);
  const [isItalic, setIsItalic] = useState<boolean>(false);
  const [isUnderline, setIsUnderline] = useState<boolean>(false);
  const [audioFile, setAudioFile] = useState<File | null>(null);

  const resetStyles = () => {
    setFontSize(defaultState.fontSize);
    setFontStyle(defaultState.fontStyle);
    setFontColor(defaultState.fontColor);
    setLineHeight(defaultState.lineHeight);
    setWordSpacing(defaultState.wordSpacing);
    // Add any additional style resets here
  };
  return (
    <TranscriptionContext.Provider
      value={{
        transcriptionData,
        setTranscriptionData,
        fontSize,
        setFontSize,
        fontStyle,
        setFontStyle,
        fontColor,
        setFontColor,
        highlightColor,
        setHighlightColor,
        lineHeight,
        setLineHeight,
        wordSpacing,
        setWordSpacing,
        isBold,
        setIsBold,
        isItalic,
        setIsItalic,
        isUnderline,
        setIsUnderline,
        resetStyles,
        audioFile,
        setAudioFile,
      }}
    >
      {children}
    </TranscriptionContext.Provider>
  );
};

export const useTranscription = () => useContext(TranscriptionContext);
