(* Content-type: application/vnd.wolfram.cdf.text *)

(*** Wolfram CDF File ***)
(* http://www.wolfram.com/cdf *)

(* CreatedBy='Mathematica 9.0' *)

(*************************************************************************)
(*                                                                       *)
(*  The Mathematica License under which this file was created prohibits  *)
(*  restricting third parties in receipt of this file from republishing  *)
(*  or redistributing it by any means, including but not limited to      *)
(*  rights management or terms of use, without the express consent of    *)
(*  Wolfram Research, Inc. For additional information concerning CDF     *)
(*  licensing and redistribution see:                                    *)
(*                                                                       *)
(*        www.wolfram.com/cdf/adopting-cdf/licensing-options.html        *)
(*                                                                       *)
(*************************************************************************)

(*CacheID: 234*)
(* Internal cache information:
NotebookFileLineBreakTest
NotebookFileLineBreakTest
NotebookDataPosition[      1063,         20]
NotebookDataLength[    252736,       5631]
NotebookOptionsPosition[    151159,       3521]
NotebookOutlinePosition[    250399,       5534]
CellTagsIndexPosition[    250356,       5531]
WindowFrame->Normal*)

(* Beginning of Notebook Content *)
Notebook[{

Cell[CellGroupData[{
Cell["Initializations", "Subtitle",
 Evaluatable->False,
 FontFamily->"Courier New",
 Background->GrayLevel[0.900008]],

Cell["\<\
These two commands turn off the spell checker, 
otherwise we get spurious messages like...\
\>", "Text",
 Evaluatable->False,
 FontFamily->"Courier New",
 Background->GrayLevel[0.900008]],

Cell[OutputFormData["\<\
Can't Format Cell













\
\>", "\<\
General::spell1: Possible spelling error: new symbol name \"llss\"
     is similar to existing symbol \"lsss\".\
\>"], "Message",
 PageWidth->Infinity,
 Evaluatable->False,
 FontFamily->"Courier New",
 FontSize->10,
 FontWeight->"Plain",
 FontSlant->"Plain",
 FontTracking->"Plain",
 FontVariations->{"Outline"->False,
 "Shadow"->False,
 "Underline"->False},
 FontColor->RGBColor[1, 0, 0],
 Background->GrayLevel[1]],

Cell[BoxData[{
 RowBox[{
  RowBox[{"Off", "[", 
   RowBox[{"General", "::", "\"\<spell\>\""}], "]"}], ";"}], "\n", 
 RowBox[{
  RowBox[{"Off", "[", 
   RowBox[{"General", "::", "\"\<spell1\>\""}], "]"}], ";"}]}], "Input",
 PageWidth->Infinity,
 FontFamily->"Courier New"],

Cell[BoxData[
 RowBox[{
  RowBox[{"$TextStyle", "=", 
   RowBox[{"{", 
    RowBox[{
     RowBox[{"FontFamily", "\[Rule]", "\"\<Times\>\""}], ",", 
     RowBox[{"FontSize", "\[Rule]", "19"}]}], "}"}]}], ";"}]], "Input",
 FontFamily->"Courier New"],

Cell[BoxData[""], "Input",
 FontFamily->"Courier New"]
}, Open  ]],

Cell["Load the graphics libraries. ", "Subtitle",
 Evaluatable->False,
 FontFamily->"Courier New",
 Background->GrayLevel[0.900008]],

Cell[CellGroupData[{

Cell[TextData[StyleBox["APERTURE functions",
 FontFamily->"Courier"]], "Title",
 Background->RGBColor[1, 1, 0]],

Cell[BoxData[" "], "Input",
 CellChangeTimes->{3.636375202710785*^9}],

Cell[CellGroupData[{

Cell["RECTANGLE", "Subtitle",
 CellChangeTimes->{3.6363725914789543`*^9},
 Background->RGBColor[1, 1, 0]],

Cell[BoxData[
 RowBox[{
  RowBox[{"RECTANGLE", "[", 
   RowBox[{
   "y_", ",", "HorEx_", ",", "HorIn_", ",", "Ver_", ",", "offset_", ",", 
    "TILT_"}], "]"}], ":=", 
  RowBox[{"Module", "[", 
   RowBox[{
    RowBox[{"{", 
     RowBox[{"f", ",", "x", ",", "offsetRay"}], "}"}], ",", 
    "\[IndentingNewLine]", "\[IndentingNewLine]", "\[IndentingNewLine]", 
    RowBox[{
     RowBox[{"offsetRay", "=", 
      RowBox[{"offset", "-", 
       RowBox[{
        RowBox[{"(", 
         RowBox[{"HorEx", "-", "HorIn"}], ")"}], "/", "2."}]}]}], ";", 
     "\[IndentingNewLine]", "\[IndentingNewLine]", "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{"0", "/;", " ", 
       RowBox[{"x", " ", ">", " ", 
        RowBox[{"HorEx", "+", "offsetRay"}]}]}]}], ";", "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{"Ver", "/;", " ", 
       RowBox[{
        RowBox[{"x", " ", "\[LessEqual]", "  ", 
         RowBox[{"HorEx", "+", "offsetRay"}]}], " ", "&&", " ", 
        RowBox[{"x", " ", ">", " ", 
         RowBox[{
          RowBox[{"-", "HorIn"}], "+", "offsetRay"}]}]}]}]}], " ", ";", 
     "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{"0", "/;", " ", 
       RowBox[{"x", " ", "\[LessEqual]", 
        RowBox[{
         RowBox[{"-", "HorIn"}], "+", "offsetRay"}]}]}]}], ";", " ", 
     "\[IndentingNewLine]", "\[IndentingNewLine]", 
     RowBox[{"If", "[", 
      RowBox[{
       RowBox[{"TILT", "\[Equal]", "0"}], ",", 
       RowBox[{"{", 
        RowBox[{"y", ",", 
         RowBox[{"f", "[", "y", "]"}]}], "}"}], ",", 
       RowBox[{"{", 
        RowBox[{
         RowBox[{
          RowBox[{"y", "*", 
           RowBox[{"Cos", "[", "TILT", "]"}]}], "-", 
          RowBox[{
           RowBox[{"f", "[", "y", "]"}], "*", 
           RowBox[{"Sin", "[", "TILT", "]"}]}]}], ",", 
         RowBox[{
          RowBox[{"y", "*", 
           RowBox[{"Sin", "[", "TILT", "]"}]}], "+", 
          RowBox[{
           RowBox[{"f", "[", "y", "]"}], "*", 
           RowBox[{"Cos", "[", "TILT", "]"}]}]}]}], "}"}]}], "]"}]}]}], 
   "]"}]}]], "Input",
 CellChangeTimes->{{3.6327254774159546`*^9, 3.6327254783979774`*^9}, {
   3.6327255293309975`*^9, 3.6327255306110234`*^9}, {3.6327256577445745`*^9, 
   3.632725661808675*^9}, {3.636372573335806*^9, 3.6363725837724066`*^9}, 
   3.636372680541067*^9, {3.636372895388399*^9, 3.636372908913859*^9}, {
   3.6363729497554445`*^9, 3.6363729517210817`*^9}, {3.6363730858056602`*^9, 
   3.6363730980206957`*^9}, {3.6363731306253223`*^9, 3.636373180156275*^9}, {
   3.6363732248979354`*^9, 3.6363732463171473`*^9}, {3.636374626588493*^9, 
   3.636374630301364*^9}, {3.6363746716421595`*^9, 3.6363746763222494`*^9}}],

Cell[CellGroupData[{

Cell[TextData[StyleBox["Rectellipse", "Subtitle"]], "Section",
 Background->RGBColor[1, 1, 0]],

Cell[BoxData[
 RowBox[{
  RowBox[{"Rectellipse", "[", 
   RowBox[{
   "y_", ",", "APER1_", ",", "APER2_", ",", "APER3_", ",", "APER4_", ",", 
    "TILT_"}], "]"}], ":=", 
  RowBox[{"Module", "[", 
   RowBox[{
    RowBox[{"{", 
     RowBox[{"f", ",", "x", ",", "X"}], "}"}], ",", "\[IndentingNewLine]", 
    RowBox[{
     RowBox[{"X", "=", 
      RowBox[{"APER3", "*", 
       RowBox[{"Sqrt", "[", 
        RowBox[{"1", "-", 
         RowBox[{
          RowBox[{"(", 
           RowBox[{"APER2", "/", "APER4"}], ")"}], "^", "2"}]}], "]"}]}]}], 
     ";", "\[IndentingNewLine]", "\[IndentingNewLine]", 
     RowBox[{"If", "[", 
      RowBox[{
       RowBox[{"APER1", ">=", "APER3"}], ",", "\[IndentingNewLine]", 
       RowBox[{
        RowBox[{"If", "[", 
         RowBox[{
          RowBox[{"X", "\[Element]", " ", "Reals"}], ",", 
          "\[IndentingNewLine]", 
          RowBox[{
           RowBox[{
            RowBox[{"f", "[", "x_", "]"}], ":=", " ", 
            RowBox[{"APER2", " ", "/;", " ", 
             RowBox[{
              RowBox[{"x", " ", "\[GreaterEqual]", " ", "0"}], "  ", "&&", 
              " ", 
              RowBox[{"x", " ", "\[LessEqual]", " ", "X"}]}]}]}], ";", 
           "\[IndentingNewLine]", 
           RowBox[{
            RowBox[{"f", "[", "x_", "]"}], ":=", " ", 
            RowBox[{
             RowBox[{"APER4", "*", 
              RowBox[{"Sqrt", "[", 
               RowBox[{"1", "-", 
                RowBox[{"x", "*", 
                 RowBox[{"x", "/", 
                  RowBox[{"(", 
                   RowBox[{"APER3", "*", "APER3"}], ")"}]}]}]}], "]"}]}], 
             "   ", "/;", " ", 
             RowBox[{
              RowBox[{"x", ">", "X"}], " ", "&&", " ", 
              RowBox[{"x", "\[LessEqual]", " ", "APER3"}]}]}]}], ";", 
           "\[IndentingNewLine]", 
           RowBox[{
            RowBox[{"f", "[", "x_", "]"}], ":=", 
            RowBox[{"0", " ", "/;", " ", 
             RowBox[{"x", ">", "APER3"}]}]}], ";", "\[IndentingNewLine]", 
           RowBox[{
            RowBox[{"f", "[", "x_", "]"}], ":=", 
            RowBox[{
             RowBox[{"f", "[", 
              RowBox[{"-", "x"}], "]"}], " ", "/;", " ", 
             RowBox[{"x", "<", "0"}]}]}], ";"}], ",", "\[IndentingNewLine]", 
          "\[IndentingNewLine]", 
          RowBox[{
           RowBox[{
            RowBox[{"f", "[", "x_", "]"}], ":=", " ", 
            RowBox[{
             RowBox[{"APER4", "*", 
              RowBox[{"Sqrt", "[", 
               RowBox[{"1", "-", 
                RowBox[{"x", "*", 
                 RowBox[{"x", "/", 
                  RowBox[{"(", 
                   RowBox[{"APER3", "*", "APER3"}], ")"}]}]}]}], "]"}]}], 
             "   ", "/;", " ", 
             RowBox[{
              RowBox[{"x", ">", "0"}], " ", "&&", " ", 
              RowBox[{"x", "\[LessEqual]", " ", "APER3"}]}]}]}], ";", 
           "\[IndentingNewLine]", 
           RowBox[{
            RowBox[{"f", "[", "x_", "]"}], ":=", 
            RowBox[{"0", " ", "/;", " ", 
             RowBox[{"x", ">", "APER3"}]}]}], ";", "\[IndentingNewLine]", 
           RowBox[{
            RowBox[{"f", "[", "x_", "]"}], ":=", 
            RowBox[{
             RowBox[{"f", "[", 
              RowBox[{"-", "x"}], "]"}], " ", "/;", " ", 
             RowBox[{"x", "<", "0"}]}]}], ";"}]}], "]"}], ";"}]}], 
      "\[IndentingNewLine]", "]"}], ";", "\[IndentingNewLine]", 
     "\[IndentingNewLine]", 
     RowBox[{"If", "[", 
      RowBox[{
       RowBox[{"APER1", "<", "APER3"}], ",", "\[IndentingNewLine]", 
       RowBox[{
        RowBox[{"If", "[", 
         RowBox[{
          RowBox[{"X", "\[Element]", " ", "Reals"}], ",", 
          "\[IndentingNewLine]", 
          RowBox[{
           RowBox[{"If", "[", 
            RowBox[{
             RowBox[{"X", "\[GreaterEqual]", " ", "APER1"}], ",", 
             "\[IndentingNewLine]", 
             RowBox[{
              RowBox[{
               RowBox[{"f", "[", "x_", "]"}], ":=", " ", 
               RowBox[{"APER2", " ", "/;", " ", 
                RowBox[{
                 RowBox[{"x", " ", "\[GreaterEqual]", " ", "0"}], "  ", "&&", 
                 " ", 
                 RowBox[{"x", " ", "\[LessEqual]", " ", "APER1"}]}]}]}], ";", 
              "\[IndentingNewLine]", 
              RowBox[{
               RowBox[{"f", "[", "x_", "]"}], ":=", " ", 
               RowBox[{
                RowBox[{"10000", "*", "APER2", "*", 
                 RowBox[{"(", 
                  RowBox[{"APER1", "+", "0.0001", "-", "x"}], ")"}]}], "   ", 
                "/;", " ", 
                RowBox[{
                 RowBox[{"x", ">", "APER1"}], " ", "&&", " ", 
                 RowBox[{"x", "\[LessEqual]", " ", 
                  RowBox[{"APER1", "+", "0.0001"}]}]}]}]}], ";", 
              "\[IndentingNewLine]", 
              RowBox[{
               RowBox[{"f", "[", "x_", "]"}], ":=", 
               RowBox[{"0", " ", "/;", " ", 
                RowBox[{"x", ">", 
                 RowBox[{"APER1", "+", "0.0001"}]}]}]}], ";", 
              "\[IndentingNewLine]", 
              RowBox[{
               RowBox[{"f", "[", "x_", "]"}], ":=", 
               RowBox[{
                RowBox[{"f", "[", 
                 RowBox[{"-", "x"}], "]"}], " ", "/;", " ", 
                RowBox[{"x", "<", "0"}]}]}], ";"}], ",", 
             "\[IndentingNewLine]", "\[IndentingNewLine]", 
             RowBox[{
              RowBox[{
               RowBox[{"f", "[", "x_", "]"}], ":=", " ", 
               RowBox[{"APER2", " ", "/;", " ", 
                RowBox[{
                 RowBox[{"x", " ", "\[GreaterEqual]", " ", "0"}], "  ", "&&", 
                 " ", 
                 RowBox[{"x", " ", "\[LessEqual]", " ", "X"}]}]}]}], ";", 
              "\[IndentingNewLine]", 
              RowBox[{
               RowBox[{"f", "[", "x_", "]"}], ":=", " ", 
               RowBox[{
                RowBox[{"APER4", "*", 
                 RowBox[{"Sqrt", "[", 
                  RowBox[{"1", "-", 
                   RowBox[{"x", "*", 
                    RowBox[{"x", "/", 
                    RowBox[{"(", 
                    RowBox[{"APER3", "*", "APER3"}], ")"}]}]}]}], "]"}]}], 
                "   ", "/;", " ", 
                RowBox[{
                 RowBox[{"x", ">", "X"}], " ", "&&", " ", 
                 RowBox[{"x", "\[LessEqual]", " ", "APER1"}]}]}]}], ";", 
              "\[IndentingNewLine]", 
              RowBox[{
               RowBox[{"f", "[", "x_", "]"}], ":=", 
               RowBox[{
                RowBox[{"10000", "*", "APER4", "*", 
                 RowBox[{"Sqrt", "[", 
                  RowBox[{"1", "-", 
                   RowBox[{
                    RowBox[{"APER1", "^", "2"}], "/", 
                    RowBox[{"(", 
                    RowBox[{"APER3", "^", "2"}], ")"}]}]}], "]"}], "*", 
                 RowBox[{"(", 
                  RowBox[{"APER1", "+", "0.0001", "-", "x"}], ")"}]}], "    ",
                 "/;", " ", 
                RowBox[{
                 RowBox[{"x", ">", "APER1"}], " ", "&&", " ", 
                 RowBox[{"x", "\[LessEqual]", " ", 
                  RowBox[{"APER1", "+", "0.0001"}]}]}]}]}], ";", 
              "\[IndentingNewLine]", 
              RowBox[{
               RowBox[{"f", "[", "x_", "]"}], ":=", 
               RowBox[{"0", " ", "/;", " ", 
                RowBox[{"x", ">", 
                 RowBox[{"APER1", "+", "0.0001"}]}]}]}], ";", 
              "\[IndentingNewLine]", 
              RowBox[{
               RowBox[{"f", "[", "x_", "]"}], ":=", 
               RowBox[{
                RowBox[{"f", "[", 
                 RowBox[{"-", "x"}], "]"}], " ", "/;", " ", 
                RowBox[{"x", "<", "0"}]}]}], ";"}]}], "\[IndentingNewLine]", 
            "]"}], ";"}], ",", "\[IndentingNewLine]", "\[IndentingNewLine]", 
          RowBox[{
           RowBox[{
            RowBox[{"f", "[", "x_", "]"}], ":=", " ", 
            RowBox[{
             RowBox[{"APER4", "*", 
              RowBox[{"Sqrt", "[", 
               RowBox[{"1", "-", 
                RowBox[{"x", "*", 
                 RowBox[{"x", "/", 
                  RowBox[{"(", 
                   RowBox[{"APER3", "*", "APER3"}], ")"}]}]}]}], "]"}]}], 
             "   ", "/;", "  ", 
             RowBox[{
              RowBox[{"x", " ", "\[GreaterEqual]", " ", "0"}], "  ", "&&", 
              " ", 
              RowBox[{"x", "\[LessEqual]", " ", "APER1"}]}]}]}], ";", 
           "\[IndentingNewLine]", 
           RowBox[{
            RowBox[{"f", "[", "x_", "]"}], ":=", " ", 
            RowBox[{
             RowBox[{"10000", "*", "APER4", "*", 
              RowBox[{"Sqrt", "[", 
               RowBox[{"1", "-", 
                RowBox[{
                 RowBox[{"APER1", "^", "2"}], "/", 
                 RowBox[{"(", 
                  RowBox[{"APER3", "^", "2"}], ")"}]}]}], "]"}], "*", 
              RowBox[{"(", 
               RowBox[{"APER1", "+", "0.0001", "-", "x"}], ")"}]}], "    ", "/;",
              " ", 
             RowBox[{
              RowBox[{"x", ">", "APER1"}], " ", "&&", " ", 
              RowBox[{"x", "\[LessEqual]", " ", 
               RowBox[{"APER1", "+", "0.0001"}]}]}]}]}], ";", 
           "\[IndentingNewLine]", 
           RowBox[{
            RowBox[{"f", "[", "x_", "]"}], ":=", 
            RowBox[{"0", " ", "/;", " ", 
             RowBox[{"x", ">", 
              RowBox[{"APER1", "+", "0.0001"}]}]}]}], ";", 
           "\[IndentingNewLine]", 
           RowBox[{
            RowBox[{"f", "[", "x_", "]"}], ":=", 
            RowBox[{
             RowBox[{"f", "[", 
              RowBox[{"-", "x"}], "]"}], " ", "/;", " ", 
             RowBox[{"x", "<", "0"}]}]}], ";"}]}], "\[IndentingNewLine]", 
         "]"}], ";"}]}], "\[IndentingNewLine]", "]"}], ";", 
     "\[IndentingNewLine]", "\[IndentingNewLine]", 
     RowBox[{"If", "[", 
      RowBox[{
       RowBox[{"TILT", "\[Equal]", "0"}], ",", 
       RowBox[{"{", 
        RowBox[{"y", ",", 
         RowBox[{"f", "[", "y", "]"}]}], "}"}], ",", 
       RowBox[{"{", 
        RowBox[{
         RowBox[{
          RowBox[{"y", "*", 
           RowBox[{"Cos", "[", "TILT", "]"}]}], "-", 
          RowBox[{
           RowBox[{"f", "[", "y", "]"}], "*", 
           RowBox[{"Sin", "[", "TILT", "]"}]}]}], ",", 
         RowBox[{
          RowBox[{"y", "*", 
           RowBox[{"Sin", "[", "TILT", "]"}]}], "+", 
          RowBox[{
           RowBox[{"f", "[", "y", "]"}], "*", 
           RowBox[{"Cos", "[", "TILT", "]"}]}]}]}], "}"}]}], "]"}]}]}], 
   "]"}]}]], "Input"]
}, Open  ]],

Cell[CellGroupData[{

Cell[TextData[Cell[BoxData["RhombeCircle"], "Input"]], "Section",
 Background->RGBColor[1, 1, 0]],

Cell[BoxData[
 RowBox[{
  RowBox[{"RhombeCircle", "[", 
   RowBox[{
   "y_", ",", "Hor_", ",", "Ver_", ",", "Rh_", ",", "Rv_", ",", "L_", ",", 
    " ", "TILT_"}], "]"}], ":=", 
  RowBox[{"Module", "[", 
   RowBox[{
    RowBox[{"{", 
     RowBox[{"f", ",", "x", ",", "h", ",", "v"}], "}"}], ",", 
    "\[IndentingNewLine]", 
    RowBox[{
     RowBox[{"If", "[", 
      RowBox[{
       RowBox[{"L", " ", "\[Equal]", "0"}], "  ", ",", "\[IndentingNewLine]", 
       
       RowBox[{
        RowBox[{"h", "=", 
         RowBox[{
          RowBox[{"(", 
           RowBox[{"Hor", "-", 
            RowBox[{"2", "*", "Rh"}]}], ")"}], "/", "2"}]}], ";", " ", 
        StyleBox[
         RowBox[{"(*", " ", 
          RowBox[{
           RowBox[{"distance", " ", "from", " ", 
            RowBox[{"(", 
             RowBox[{"0", ",", "0"}], ")"}], " ", "to", " ", "centrum", " ", 
            "of", " ", "circle", " ", "on", " ", "x"}], "-", 
           RowBox[{"axis", " ", 
            RowBox[{"(", "hor", ")"}]}]}], " ", "*)"}],
         FontColor->RGBColor[0, 0, 1]], "\[IndentingNewLine]", 
        RowBox[{"v", "=", 
         RowBox[{
          RowBox[{"(", 
           RowBox[{"Ver", "-", 
            RowBox[{"2", "*", "Rv"}]}], ")"}], "/", "2"}]}], ";", " ", 
        StyleBox[
         RowBox[{"(*", " ", 
          RowBox[{
           RowBox[{"distance", " ", "from", " ", 
            RowBox[{"(", 
             RowBox[{"0", ",", "0"}], ")"}], " ", "to", " ", "centrum", " ", 
            "of", " ", "circle", " ", "on", " ", "y"}], "-", 
           RowBox[{"axis", " ", 
            RowBox[{"(", "ver", ")"}]}]}], " ", "*)"}],
         FontColor->RGBColor[0, 0, 1]], "\[IndentingNewLine]", 
        RowBox[{"sin1", "=", 
         FractionBox[
          RowBox[{
           RowBox[{"Rh", " ", "v"}], "-", 
           RowBox[{"Rv", " ", "v"}], "-", 
           SqrtBox[
            RowBox[{
             SuperscriptBox["h", "4"], "-", 
             RowBox[{
              SuperscriptBox["h", "2"], " ", 
              SuperscriptBox["Rh", "2"]}], "+", 
             RowBox[{"2", " ", 
              SuperscriptBox["h", "2"], " ", "Rh", " ", "Rv"}], "-", 
             RowBox[{
              SuperscriptBox["h", "2"], " ", 
              SuperscriptBox["Rv", "2"]}], "+", 
             RowBox[{
              SuperscriptBox["h", "2"], " ", 
              SuperscriptBox["v", "2"]}]}]]}], 
          RowBox[{
           SuperscriptBox["h", "2"], "+", 
           SuperscriptBox["v", "2"]}]]}], ";", "\[IndentingNewLine]", 
        RowBox[{"sin2", "=", 
         FractionBox[
          RowBox[{
           RowBox[{"Rh", " ", "v"}], "-", 
           RowBox[{"Rv", " ", "v"}], "+", 
           SqrtBox[
            RowBox[{
             SuperscriptBox["h", "4"], "-", 
             RowBox[{
              SuperscriptBox["h", "2"], " ", 
              SuperscriptBox["Rh", "2"]}], "+", 
             RowBox[{"2", " ", 
              SuperscriptBox["h", "2"], " ", "Rh", " ", "Rv"}], "-", 
             RowBox[{
              SuperscriptBox["h", "2"], " ", 
              SuperscriptBox["Rv", "2"]}], "+", 
             RowBox[{
              SuperscriptBox["h", "2"], " ", 
              SuperscriptBox["v", "2"]}]}]]}], 
          RowBox[{
           SuperscriptBox["h", "2"], "+", 
           SuperscriptBox["v", "2"]}]]}], ";", "\[IndentingNewLine]", 
        "\[IndentingNewLine]", 
        RowBox[{"sin", "=", 
         RowBox[{"If", "[", 
          RowBox[{
           RowBox[{"sin1", ">", "sin2"}], ",", 
           RowBox[{"sin1", "*", "1.0"}], ",", 
           RowBox[{"sin2", "*", "1.0"}]}], "]"}]}], ";", 
        "\[IndentingNewLine]", 
        RowBox[{"cos", "=", 
         RowBox[{"Sqrt", "[", 
          RowBox[{"1", "-", 
           RowBox[{"sin", "^", "2"}]}], "]"}]}], ";", "\[IndentingNewLine]", 
        RowBox[{"(*", " ", 
         RowBox[{
          RowBox[{"Print", "[", 
           RowBox[{
           "\"\<sin=\>\"", ",", "sin", ",", "\"\<   cos=\>\"", ",", "cos"}], 
           "]"}], ";"}], " ", "*)"}], "\[IndentingNewLine]", 
        "\[IndentingNewLine]", 
        RowBox[{
         RowBox[{"f", "[", "x_", "]"}], ":=", " ", 
         RowBox[{
          RowBox[{
           RowBox[{"Sqrt", "[", 
            RowBox[{
             RowBox[{"Rv", "^", "2"}], "-", 
             RowBox[{"x", "^", "2"}]}], "]"}], "+", "v"}], " ", "/;", " ", 
          RowBox[{
           RowBox[{"x", " ", "\[GreaterEqual]", " ", "0"}], " ", "&&", " ", 
           RowBox[{"x", " ", "\[LessEqual]", 
            RowBox[{"Rv", "*", "cos"}]}]}]}]}], " ", ";", 
        RowBox[{
         RowBox[{"f", "[", "x_", "]"}], ":=", " ", 
         RowBox[{
          RowBox[{
           RowBox[{
            RowBox[{"(", 
             RowBox[{
              RowBox[{"(", 
               RowBox[{
                RowBox[{
                 RowBox[{"(", 
                  RowBox[{"Rh", "-", "Rv"}], ")"}], "*", "sin"}], "-", "v"}], 
               ")"}], "/", 
              RowBox[{"(", 
               RowBox[{
                RowBox[{
                 RowBox[{"(", 
                  RowBox[{"Rh", "-", "Rv"}], ")"}], "*", "cos"}], "+", "h"}], 
               ")"}]}], ")"}], "*", 
            RowBox[{"(", 
             RowBox[{"x", "-", 
              RowBox[{"Rh", "*", "cos"}], "-", "h"}], ")"}]}], "+", " ", 
           RowBox[{"Rh", "*", "sin"}]}], " ", "/;", " ", 
          RowBox[{
           RowBox[{"x", ">", 
            RowBox[{"Rh", "*", "cos"}]}], " ", "&&", " ", 
           RowBox[{"x", "\[LessEqual]", " ", 
            RowBox[{
             RowBox[{"Rh", "*", "cos"}], "+", "h"}]}]}]}]}], ";", 
        "\[IndentingNewLine]", 
        RowBox[{
         RowBox[{"f", "[", "x_", "]"}], ":=", " ", 
         RowBox[{
          RowBox[{"Sqrt", "[", 
           RowBox[{
            RowBox[{"Rh", "^", "2"}], "-", 
            RowBox[{
             RowBox[{"(", 
              RowBox[{"x", "-", "h"}], ")"}], "^", "2"}]}], "]"}], " ", "/;", 
          " ", 
          RowBox[{
           RowBox[{"x", "\[GreaterEqual]", " ", 
            RowBox[{
             RowBox[{"Rh", "*", "cos"}], "+", "h"}]}], " ", "&&", " ", 
           RowBox[{"x", " ", "\[LessEqual]", " ", 
            RowBox[{"Hor", "/", "2"}]}]}]}]}], ";", "\[IndentingNewLine]", 
        RowBox[{
         RowBox[{"f", "[", "x_", "]"}], ":=", 
         RowBox[{"0", " ", "/;", " ", 
          RowBox[{"x", ">", 
           RowBox[{"Hor", "/", "2"}]}]}]}], ";"}], "\[IndentingNewLine]", ",",
        "\[IndentingNewLine]", 
       RowBox[{
        RowBox[{
         RowBox[{"yL", "[", "x_", "]"}], "=", 
         RowBox[{
          RowBox[{"-", "1"}], "*", 
          RowBox[{"(", 
           RowBox[{"x", "-", 
            RowBox[{
             FractionBox["1", "2"], 
             SqrtBox[
              RowBox[{"2", "*", 
               SuperscriptBox["L", "2"]}]]}]}], ")"}]}]}], ";", 
        "\[IndentingNewLine]", 
        RowBox[{
         RowBox[{"yH", "[", "x_", "]"}], "=", 
         SqrtBox[
          RowBox[{
           RowBox[{"Rh", "^", "2"}], "-", 
           RowBox[{
            RowBox[{"(", 
             RowBox[{"x", "-", 
              RowBox[{"(", 
               RowBox[{
                RowBox[{"Hor", "/", "2"}], "-", "Rh"}], ")"}]}], ")"}], "^", 
            "2"}]}]]}], ";", "\[IndentingNewLine]", 
        RowBox[{
         RowBox[{"yV", "[", "x_", "]"}], "=", 
         RowBox[{
          SqrtBox[
           RowBox[{
            RowBox[{"Rv", "^", "2"}], "-", 
            RowBox[{"x", "^", "2"}]}]], "+", 
          RowBox[{"Ver", "/", "2"}], "-", "Rv"}]}], ";", 
        "\[IndentingNewLine]", "\[IndentingNewLine]", 
        RowBox[{"Off", "[", 
         RowBox[{"FindMinimum", "::", "\"\<lstol\>\""}], "]"}], ";", 
        "\[IndentingNewLine]", 
        RowBox[{"solV", "=", 
         RowBox[{"FindMinimum", "[", 
          RowBox[{
           RowBox[{
            RowBox[{"(", 
             RowBox[{
              RowBox[{"yL", "[", "x", "]"}], "-", 
              RowBox[{"yV", "[", "x", "]"}]}], ")"}], "*", 
            RowBox[{"Conjugate", "[", 
             RowBox[{
              RowBox[{"yL", "[", "x", "]"}], "-", 
              RowBox[{"yV", "[", "x", "]"}]}], "]"}]}], ",", 
           RowBox[{"{", 
            RowBox[{"x", ",", "0"}], "}"}]}], "]"}]}], ";", 
        "\[IndentingNewLine]", 
        RowBox[{"solH", "=", 
         RowBox[{"FindMinimum", "[", 
          RowBox[{
           RowBox[{
            RowBox[{"(", 
             RowBox[{
              RowBox[{"yL", "[", "x", "]"}], "-", 
              RowBox[{"yH", "[", "x", "]"}]}], ")"}], "*", 
            RowBox[{"Conjugate", "[", 
             RowBox[{
              RowBox[{"yL", "[", "x", "]"}], "-", 
              RowBox[{"yH", "[", "x", "]"}]}], "]"}]}], ",", " ", 
           RowBox[{"{", 
            RowBox[{"x", ",", 
             RowBox[{"Hor", "/", "2"}]}], "}"}]}], "]"}]}], ";", 
        "\[IndentingNewLine]", 
        RowBox[{"On", "[", 
         RowBox[{"FindMinimum", "::", "\"\<lstol\>\""}], "]"}], ";", 
        "\[IndentingNewLine]", 
        RowBox[{"(*", " ", 
         RowBox[{
          RowBox[{"Print", "[", 
           RowBox[{
           "\"\<solH=\>\"", ",", "solH", ",", "\"\<   solV=\>\"", ",", 
            "solV"}], "]"}], ";"}], " ", "*)"}], "\[IndentingNewLine]", 
        "\[IndentingNewLine]", 
        RowBox[{
         RowBox[{"f", "[", "x_", "]"}], ":=", 
         RowBox[{
          RowBox[{"yV", "[", "x", "]"}], "/;", 
          RowBox[{
           RowBox[{"x", " ", ">", "0"}], " ", "&&", " ", 
           RowBox[{"x", "<", " ", 
            RowBox[{
             RowBox[{
              RowBox[{"solV", "[", 
               RowBox[{"[", "2", "]"}], "]"}], "[", 
              RowBox[{"[", "1", "]"}], "]"}], "[", 
             RowBox[{"[", "2", "]"}], "]"}]}]}]}]}], ";", 
        "\[IndentingNewLine]", 
        RowBox[{
         RowBox[{"f", "[", "x_", "]"}], ":=", 
         RowBox[{
          RowBox[{"yL", "[", "x", "]"}], "/;", 
          RowBox[{
           RowBox[{"x", " ", ">", 
            RowBox[{
             RowBox[{
              RowBox[{"solV", "[", 
               RowBox[{"[", "2", "]"}], "]"}], "[", 
              RowBox[{"[", "1", "]"}], "]"}], "[", 
             RowBox[{"[", "2", "]"}], "]"}]}], "  ", "&&", " ", 
           RowBox[{"x", " ", "\[LessEqual]", " ", 
            RowBox[{
             RowBox[{
              RowBox[{"solH", "[", 
               RowBox[{"[", "2", "]"}], "]"}], "[", 
              RowBox[{"[", "1", "]"}], "]"}], "[", 
             RowBox[{"[", "2", "]"}], "]"}]}]}]}]}], ";", 
        "\[IndentingNewLine]", 
        RowBox[{
         RowBox[{"f", "[", "x_", "]"}], ":=", 
         RowBox[{
          RowBox[{"yH", "[", "x", "]"}], "/;", 
          RowBox[{
           RowBox[{"x", " ", ">", "   ", 
            RowBox[{
             RowBox[{
              RowBox[{"solH", "[", 
               RowBox[{"[", "2", "]"}], "]"}], "[", 
              RowBox[{"[", "1", "]"}], "]"}], "[", 
             RowBox[{"[", "2", "]"}], "]"}]}], "  ", "&&", " ", 
           RowBox[{"x", " ", "\[LessEqual]", " ", 
            RowBox[{"Hor", "/", "2"}]}]}]}]}], ";", "\[IndentingNewLine]", 
        RowBox[{
         RowBox[{"f", "[", "x_", "]"}], ":=", 
         RowBox[{"0", " ", "/;", " ", 
          RowBox[{"x", ">", 
           RowBox[{"Hor", "/", "2"}]}]}]}], ";"}]}], "\[IndentingNewLine]", 
      "]"}], ";", "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{
       RowBox[{"f", "[", 
        RowBox[{"-", "x"}], "]"}], " ", "/;", " ", 
       RowBox[{"x", "<", "0"}]}]}], ";", "\[IndentingNewLine]", 
     RowBox[{"If", "[", 
      RowBox[{
       RowBox[{"TILT", "\[Equal]", "0"}], ",", 
       RowBox[{"{", 
        RowBox[{"y", ",", 
         RowBox[{"f", "[", "y", "]"}]}], "}"}], ",", 
       RowBox[{"{", 
        RowBox[{
         RowBox[{
          RowBox[{"y", "*", 
           RowBox[{"Cos", "[", "TILT", "]"}]}], "-", 
          RowBox[{
           RowBox[{"f", "[", "y", "]"}], "*", 
           RowBox[{"Sin", "[", "TILT", "]"}]}]}], ",", 
         RowBox[{
          RowBox[{"y", "*", 
           RowBox[{"Sin", "[", "TILT", "]"}]}], "+", 
          RowBox[{
           RowBox[{"f", "[", "y", "]"}], "*", 
           RowBox[{"Cos", "[", "TILT", "]"}]}]}]}], "}"}]}], "]"}]}]}], 
   "]"}]}]], "Input"]
}, Open  ]],

Cell[CellGroupData[{

Cell[TextData[Cell[BoxData["Diamond"], "Input"]], "Section",
 Background->RGBColor[1, 1, 0]],

Cell[BoxData[
 RowBox[{
  RowBox[{"Diamond", "[", 
   RowBox[{"y_", ",", "Hor_", ",", "Ver_", ",", "TILT_"}], "]"}], ":=", 
  RowBox[{"Module", "[", 
   RowBox[{
    RowBox[{"{", 
     RowBox[{"f", ",", "x"}], "}"}], ",", "\[IndentingNewLine]", 
    RowBox[{
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", " ", 
      RowBox[{
       RowBox[{
        RowBox[{
         RowBox[{"(", 
          RowBox[{
           RowBox[{"-", "Ver"}], "/", "Hor"}], ")"}], "*", "x"}], "+", 
        RowBox[{"Ver", "/", "2"}]}], "    ", "/;", " ", 
       RowBox[{
        RowBox[{"x", " ", "\[GreaterEqual]", " ", "0"}], " ", "&&", "  ", 
        RowBox[{"x", "\[LessEqual]", " ", 
         RowBox[{"Hor", "/", "2"}]}]}]}]}], ";", "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{"0", " ", "/;", " ", 
       RowBox[{"x", ">", 
        RowBox[{"Hor", "/", "2"}]}]}]}], ";", "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{
       RowBox[{"f", "[", 
        RowBox[{"-", "x"}], "]"}], " ", "/;", " ", 
       RowBox[{"x", "<", "0"}]}]}], ";", "\[IndentingNewLine]", 
     RowBox[{"If", "[", 
      RowBox[{
       RowBox[{"TILT", "\[Equal]", "0"}], ",", 
       RowBox[{"{", 
        RowBox[{"y", ",", 
         RowBox[{"f", "[", "y", "]"}]}], "}"}], ",", 
       RowBox[{"{", 
        RowBox[{
         RowBox[{
          RowBox[{"y", "*", 
           RowBox[{"Cos", "[", "TILT", "]"}]}], "-", 
          RowBox[{
           RowBox[{"f", "[", "y", "]"}], "*", 
           RowBox[{"Sin", "[", "TILT", "]"}]}]}], ",", 
         RowBox[{
          RowBox[{"y", "*", 
           RowBox[{"Sin", "[", "TILT", "]"}]}], "+", 
          RowBox[{
           RowBox[{"f", "[", "y", "]"}], "*", 
           RowBox[{"Cos", "[", "TILT", "]"}]}]}]}], "}"}]}], "]"}]}]}], 
   "]"}]}]], "Input"]
}, Open  ]],

Cell[CellGroupData[{

Cell[TextData[Cell[BoxData["Ellipse"], "Input"]], "Section",
 Background->RGBColor[1, 1, 0]],

Cell[BoxData[
 RowBox[{
  RowBox[{"Ellipse", "[", 
   RowBox[{"y_", ",", "Hor_", ",", "Ver_", ",", "TILT_"}], "]"}], ":=", 
  RowBox[{"Module", "[", 
   RowBox[{
    RowBox[{"{", 
     RowBox[{"f", ",", "x"}], "}"}], ",", "\[IndentingNewLine]", 
    RowBox[{
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", " ", 
      RowBox[{
       RowBox[{
        RowBox[{"(", 
         RowBox[{"Ver", "/", "2"}], ")"}], "*", 
        RowBox[{"Sqrt", "[", 
         RowBox[{"1", "-", 
          RowBox[{"x", "*", 
           RowBox[{"x", "/", 
            RowBox[{"(", 
             RowBox[{"Hor", "*", 
              RowBox[{"Hor", "/", "4"}]}], ")"}]}]}]}], "]"}]}], "    ", "/;",
        " ", 
       RowBox[{
        RowBox[{"x", " ", "\[GreaterEqual]", " ", "0"}], " ", "&&", "  ", 
        RowBox[{"x", "\[LessEqual]", " ", 
         RowBox[{"Hor", "/", "2"}]}]}]}]}], ";", "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{"0", " ", "/;", " ", 
       RowBox[{"x", ">", 
        RowBox[{"Hor", "/", "2"}]}]}]}], ";", "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{
       RowBox[{"f", "[", 
        RowBox[{"-", "x"}], "]"}], " ", "/;", " ", 
       RowBox[{"x", "<", "0"}]}]}], ";", "\[IndentingNewLine]", 
     RowBox[{"If", "[", 
      RowBox[{
       RowBox[{"TILT", "\[Equal]", "0"}], ",", 
       RowBox[{"{", 
        RowBox[{"y", ",", 
         RowBox[{"f", "[", "y", "]"}]}], "}"}], ",", 
       RowBox[{"{", 
        RowBox[{
         RowBox[{
          RowBox[{"y", "*", 
           RowBox[{"Cos", "[", "TILT", "]"}]}], "-", 
          RowBox[{
           RowBox[{"f", "[", "y", "]"}], "*", 
           RowBox[{"Sin", "[", "TILT", "]"}]}]}], ",", 
         RowBox[{
          RowBox[{"y", "*", 
           RowBox[{"Sin", "[", "TILT", "]"}]}], "+", 
          RowBox[{
           RowBox[{"f", "[", "y", "]"}], "*", 
           RowBox[{"Cos", "[", "TILT", "]"}]}]}]}], "}"}]}], "]"}]}]}], 
   "]"}]}]], "Input"]
}, Open  ]],

Cell[CellGroupData[{

Cell[TextData[Cell[BoxData["Racetrack"], "Input"]], "Section",
 Background->RGBColor[1, 1, 0]],

Cell[BoxData[
 RowBox[{
  RowBox[{"Racetrack", "[", 
   RowBox[{"y_", ",", "Hor_", ",", "Ver_", ",", "R_", ",", "TILT_"}], "]"}], ":=", 
  RowBox[{"Module", "[", 
   RowBox[{
    RowBox[{"{", 
     RowBox[{"f", ",", "x"}], "}"}], ",", "\[IndentingNewLine]", 
    RowBox[{
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", " ", 
      RowBox[{
       RowBox[{"Ver", "/", "2"}], "    ", "/;", " ", 
       RowBox[{
        RowBox[{"x", " ", "\[GreaterEqual]", " ", "0"}], " ", "&&", "  ", 
        RowBox[{"x", "\[LessEqual]", " ", 
         RowBox[{
          RowBox[{"Hor", "/", "2"}], "-", "R"}]}]}]}]}], ";", 
     "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{
       RowBox[{"Sqrt", "[", 
        RowBox[{
         RowBox[{"R", "^", "2"}], "-", 
         RowBox[{
          RowBox[{"(", 
           RowBox[{"x", "-", 
            RowBox[{"Hor", "/", "2"}], "+", "R"}], ")"}], "^", "2"}]}], "]"}],
        " ", "/;", " ", 
       RowBox[{
        RowBox[{"x", ">", " ", 
         RowBox[{
          RowBox[{"Hor", "/", "2"}], "-", "R"}]}], " ", "&&", " ", 
        RowBox[{"x", " ", "\[LessEqual]", " ", 
         RowBox[{"Hor", "/", "2"}]}]}]}]}], ";", "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{"0", " ", "/;", " ", 
       RowBox[{"x", ">", 
        RowBox[{"Hor", "/", "2"}]}]}]}], ";", "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{
       RowBox[{"f", "[", 
        RowBox[{"-", "x"}], "]"}], " ", "/;", " ", 
       RowBox[{"x", "<", "0"}]}]}], ";", "\[IndentingNewLine]", 
     RowBox[{"If", "[", 
      RowBox[{
       RowBox[{"TILT", "\[Equal]", "0"}], ",", 
       RowBox[{"{", 
        RowBox[{"y", ",", 
         RowBox[{"f", "[", "y", "]"}]}], "}"}], ",", 
       RowBox[{"{", 
        RowBox[{
         RowBox[{
          RowBox[{"y", "*", 
           RowBox[{"Cos", "[", "TILT", "]"}]}], "-", 
          RowBox[{
           RowBox[{"f", "[", "y", "]"}], "*", 
           RowBox[{"Sin", "[", "TILT", "]"}]}]}], ",", 
         RowBox[{
          RowBox[{"y", "*", 
           RowBox[{"Sin", "[", "TILT", "]"}]}], "+", 
          RowBox[{
           RowBox[{"f", "[", "y", "]"}], "*", 
           RowBox[{"Cos", "[", "TILT", "]"}]}]}]}], "}"}]}], "]"}]}]}], 
   "]"}]}]], "Input"]
}, Open  ]],

Cell[CellGroupData[{

Cell[TextData[Cell[BoxData["PStype"], "Input"]], "Section",
 Background->RGBColor[1, 1, 0]],

Cell[BoxData[
 RowBox[{
  RowBox[{"PStype", "[", 
   RowBox[{
   "y_", ",", "HorEx_", ",", "HorIn_", ",", "Ver_", ",", "offset_", ",", 
    "RExLarge_", ",", "RExSmall_", ",", "RInLarge_", ",", "RInSmall_", ",", 
    "TILT_"}], "]"}], ":=", 
  RowBox[{"Module", "[", 
   RowBox[{
    RowBox[{"{", 
     RowBox[{
     "f", ",", "x", ",", "CExLarge", ",", "CExSmall", ",", "CInLarge", ",", 
      "CInSmall", ",", "yExL", ",", "yExS", ",", "yInL", ",", "yInS", ",", 
      "EX", ",", "IN", ",", "TestR", ",", "offsetRay"}], "}"}], ",", 
    "\[IndentingNewLine]", "\[IndentingNewLine]", 
    RowBox[{
     RowBox[{"If", "[", 
      RowBox[{
       RowBox[{
        RowBox[{"TestR", "[", 
         RowBox[{"RExSmall", ",", "RExLarge"}], "]"}], "<", "0"}], ",", 
       RowBox[{
        RowBox[{"Return", "[", 
         RowBox[{"-", "1"}], "]"}], ";"}]}], "]"}], ";", 
     "\[IndentingNewLine]", 
     RowBox[{"If", "[", 
      RowBox[{
       RowBox[{
        RowBox[{"TestR", "[", 
         RowBox[{"RInSmall", ",", "RInLarge"}], "]"}], "<", "0"}], ",", 
       RowBox[{
        RowBox[{"Return", "[", 
         RowBox[{"-", "1"}], "]"}], ";"}]}], "]"}], ";", 
     "\[IndentingNewLine]", "\[IndentingNewLine]", 
     RowBox[{"offsetRay", "=", 
      RowBox[{"offset", "-", 
       RowBox[{
        RowBox[{"(", 
         RowBox[{"HorEx", "-", "HorIn"}], ")"}], "/", "2."}]}]}], ";", 
     "\[IndentingNewLine]", 
     RowBox[{"CExLarge", "   ", "=", " ", 
      RowBox[{"{", 
       RowBox[{"offsetRay", ",", " ", 
        RowBox[{"Ver", "-", "RExLarge"}]}], " ", "}"}]}], ";", 
     "                     ", 
     StyleBox[
      RowBox[{"(*", "  ", 
       RowBox[{"[", "mm", "]"}], "   ", "*)"}],
      FontColor->RGBColor[0, 0, 1]], "\[IndentingNewLine]", 
     RowBox[{"CExSmall", "   ", "=", " ", 
      RowBox[{"{", 
       RowBox[{
        RowBox[{"offsetRay", "+", "HorEx", "-", "RExSmall"}], ",", " ", 
        "0.0"}], "}"}]}], ";", "      ", 
     StyleBox[
      RowBox[{"(*", "  ", 
       RowBox[{"[", "mm", "]"}], "   ", "*)"}],
      FontColor->RGBColor[0, 0, 1]], "\[IndentingNewLine]", 
     RowBox[{"CInLarge", "   ", "=", " ", 
      RowBox[{"{", 
       RowBox[{"offsetRay", ",", " ", 
        RowBox[{"Ver", "-", "RInLarge"}]}], " ", "}"}]}], ";", 
     "                     ", 
     StyleBox[
      RowBox[{"(*", "  ", 
       RowBox[{"[", "mm", "]"}], "   ", "*)"}],
      FontColor->RGBColor[0, 0, 1]], "\[IndentingNewLine]", 
     RowBox[{"CInSmall", "   ", "=", " ", 
      RowBox[{"{", 
       RowBox[{
        RowBox[{"offsetRay", "+", "RInSmall", "-", "HorIn"}], ",", " ", 
        "0.0"}], "}"}]}], ";", "       ", 
     StyleBox[
      RowBox[{"(*", "  ", 
       RowBox[{"[", "mm", "]"}], "   ", "*)"}],
      FontColor->RGBColor[0, 0, 1]], "\[IndentingNewLine]", 
     "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"yExL", "[", "x_", "]"}], "=", 
      RowBox[{
       SqrtBox[
        RowBox[{
         RowBox[{"RExLarge", "^", "2"}], "-", 
         RowBox[{
          RowBox[{"(", 
           RowBox[{"x", "-", 
            RowBox[{"CExLarge", "[", 
             RowBox[{"[", "1", "]"}], "]"}]}], ")"}], "^", "2"}]}]], "+", 
       RowBox[{"CExLarge", "[", 
        RowBox[{"[", "2", "]"}], "]"}]}]}], ";", "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"yExS", "[", "x_", "]"}], "=", 
      RowBox[{
       SqrtBox[
        RowBox[{
         RowBox[{"RExSmall", "^", "2"}], "-", 
         RowBox[{
          RowBox[{"(", 
           RowBox[{"x", "-", 
            RowBox[{"CExSmall", "[", 
             RowBox[{"[", "1", "]"}], "]"}]}], ")"}], "^", "2"}]}]], "+", 
       RowBox[{"CExSmall", "[", 
        RowBox[{"[", "2", "]"}], "]"}]}]}], ";", "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"yInL", "[", "x_", "]"}], "=", 
      RowBox[{
       SqrtBox[
        RowBox[{
         RowBox[{"RInLarge", "^", "2"}], "-", 
         RowBox[{
          RowBox[{"(", 
           RowBox[{"x", "-", 
            RowBox[{"CInLarge", "[", 
             RowBox[{"[", "1", "]"}], "]"}]}], ")"}], "^", "2"}]}]], "+", 
       RowBox[{"CInLarge", "[", 
        RowBox[{"[", "2", "]"}], "]"}]}]}], ";", "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"yInS", "[", "x_", "]"}], "=", 
      RowBox[{
       SqrtBox[
        RowBox[{
         RowBox[{"RInSmall", "^", "2"}], "-", 
         RowBox[{
          RowBox[{"(", 
           RowBox[{"x", "-", 
            RowBox[{"CInSmall", "[", 
             RowBox[{"[", "1", "]"}], "]"}]}], ")"}], "^", "2"}]}]], "+", 
       RowBox[{"CInSmall", "[", 
        RowBox[{"[", "2", "]"}], "]"}]}]}], ";", "\[IndentingNewLine]", 
     "\[IndentingNewLine]", 
     RowBox[{"Off", "[", 
      RowBox[{"FindMinimum", "::", "\"\<lstol\>\""}], "]"}], ";", 
     "\[IndentingNewLine]", 
     RowBox[{"EX", "=", 
      RowBox[{"FindMinimum", "[", 
       RowBox[{
        RowBox[{
         RowBox[{"(", 
          RowBox[{
           RowBox[{"yExL", "[", "x", "]"}], "-", 
           RowBox[{"yExS", "[", "x", "]"}]}], ")"}], "*", 
         RowBox[{"Conjugate", "[", 
          RowBox[{
           RowBox[{"yExL", "[", "x", "]"}], "-", 
           RowBox[{"yExS", "[", "x", "]"}]}], "]"}]}], ",", 
        RowBox[{"{", 
         RowBox[{"x", ",", 
          RowBox[{"offsetRay", "+", "HorEx", "-", 
           RowBox[{"RExSmall", "/", "2."}]}]}], "}"}]}], "]"}]}], ";", 
     "\[IndentingNewLine]", 
     RowBox[{"IN", "=", 
      RowBox[{"FindMinimum", "[", 
       RowBox[{
        RowBox[{
         RowBox[{"(", 
          RowBox[{
           RowBox[{"yInL", "[", "x", "]"}], "-", 
           RowBox[{"yInS", "[", "x", "]"}]}], ")"}], "*", 
         RowBox[{"Conjugate", "[", 
          RowBox[{
           RowBox[{"yInL", "[", "x", "]"}], "-", 
           RowBox[{"yInS", "[", "x", "]"}]}], "]"}]}], ",", " ", 
        RowBox[{"{", 
         RowBox[{"x", ",", 
          RowBox[{"offsetRay", "+", 
           RowBox[{"RInSmall", "/", "2"}], "-", "HorIn"}]}], "}"}]}], "]"}]}],
      ";", "\[IndentingNewLine]", 
     RowBox[{"On", "[", 
      RowBox[{"FindMinimum", "::", "\"\<lstol\>\""}], "]"}], ";", 
     "\[IndentingNewLine]", "\[IndentingNewLine]", 
     RowBox[{"If", "[", 
      RowBox[{
       RowBox[{
        RowBox[{"EX", "[", 
         RowBox[{"[", "1", "]"}], "]"}], ">", "5.0"}], " ", 
       RowBox[{"(*", " ", "mm", " ", "*)"}], ",", "\[IndentingNewLine]", 
       RowBox[{
        RowBox[{"Print", "[", "\"\<PStype. Error. \>\"", "]"}], ";", 
        "\[IndentingNewLine]", 
        RowBox[{"Print", "[", 
         RowBox[{"\"\<Cannot find intersection between: yExL[x]=\>\"", ",", 
          RowBox[{"yExL", "[", "x", "]"}], ",", "\"\< and yExS[x]=\>\"", ",", 
          
          RowBox[{"yExS", "[", "x", "]"}]}], "]"}], ";", 
        RowBox[{"Print", "[", 
         RowBox[{
         "\"\<  RExSmall=\>\"", ",", "RExSmall", ",", "\"\< RExLarge=\>\"", 
          ",", "RExLarge"}], "]"}], ";", "\[IndentingNewLine]", 
        RowBox[{"Return", "[", 
         RowBox[{"-", "1"}], "]"}], ";"}]}], "\[IndentingNewLine]", "]"}], 
     ";", "\[IndentingNewLine]", 
     RowBox[{"If", "[", 
      RowBox[{
       RowBox[{
        RowBox[{"IN", "[", 
         RowBox[{"[", "1", "]"}], "]"}], ">", "3.0"}], " ", 
       RowBox[{"(*", " ", "mm", " ", "*)"}], ",", "\[IndentingNewLine]", 
       RowBox[{
        RowBox[{"Print", "[", "\"\<PStype. Error. \>\"", "]"}], ";", 
        "\[IndentingNewLine]", 
        RowBox[{"Print", "[", 
         RowBox[{"\"\<Cannot find intersection between: yInL[x]=\>\"", ",", 
          RowBox[{"yInL", "[", "x", "]"}], ",", "\"\< and yInS[x]=\>\"", ",", 
          
          RowBox[{"yInS", "[", "x", "]"}]}], "]"}], ";", 
        RowBox[{"Print", "[", 
         RowBox[{
         "\"\< RInSmall=\>\"", ",", "RInSmall", ",", "\"\< RInLarge=\>\"", 
          ",", "RInLarge"}], "]"}], ";", "\[IndentingNewLine]", 
        RowBox[{"Return", "[", 
         RowBox[{"-", "1"}], "]"}], ";"}]}], "\[IndentingNewLine]", "]"}], 
     ";", "\[IndentingNewLine]", "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{"0", "/;", " ", 
       RowBox[{"x", " ", ">", " ", 
        RowBox[{"HorEx", "+", "offsetRay"}]}]}]}], ";", "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{
       RowBox[{"yExS", "[", "x", "]"}], "/;", 
       RowBox[{
        RowBox[{"x", " ", ">", " ", 
         RowBox[{
          RowBox[{
           RowBox[{"EX", "[", 
            RowBox[{"[", "2", "]"}], "]"}], "[", 
           RowBox[{"[", "1", "]"}], "]"}], "[", 
          RowBox[{"[", "2", "]"}], "]"}]}], " ", "&&", " ", 
        RowBox[{"x", " ", "\[LessEqual]", "  ", 
         RowBox[{"HorEx", "+", "offsetRay"}]}]}]}]}], ";", 
     "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{
       RowBox[{"yExL", "[", "x", "]"}], "/;", 
       RowBox[{
        RowBox[{"x", " ", ">", "offsetRay"}], " ", "&&", " ", 
        RowBox[{"x", " ", "\[LessEqual]", " ", 
         RowBox[{
          RowBox[{
           RowBox[{"EX", "[", 
            RowBox[{"[", "2", "]"}], "]"}], "[", 
           RowBox[{"[", "1", "]"}], "]"}], "[", 
          RowBox[{"[", "2", "]"}], "]"}]}]}]}]}], ";", "\[IndentingNewLine]", 
     
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{
       RowBox[{"yInL", "[", "x", "]"}], "/;", 
       RowBox[{
        RowBox[{"x", " ", ">", " ", 
         RowBox[{
          RowBox[{
           RowBox[{"IN", "[", 
            RowBox[{"[", "2", "]"}], "]"}], "[", 
           RowBox[{"[", "1", "]"}], "]"}], "[", 
          RowBox[{"[", "2", "]"}], "]"}]}], " ", "&&", " ", 
        RowBox[{"x", " ", "\[LessEqual]", " ", "offsetRay"}]}]}]}], ";", 
     "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{
       RowBox[{"yInS", "[", "x", "]"}], "/;", 
       RowBox[{
        RowBox[{"x", " ", ">", " ", 
         RowBox[{
          RowBox[{"-", "HorIn"}], "+", "offsetRay"}]}], " ", "&&", " ", 
        RowBox[{"x", " ", "\[LessEqual]", 
         RowBox[{
          RowBox[{
           RowBox[{"IN", "[", 
            RowBox[{"[", "2", "]"}], "]"}], "[", 
           RowBox[{"[", "1", "]"}], "]"}], "[", 
          RowBox[{"[", "2", "]"}], "]"}]}]}]}]}], ";", "\[IndentingNewLine]", 
     
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{"0", "/;", " ", 
       RowBox[{"x", " ", "\[LessEqual]", 
        RowBox[{
         RowBox[{"-", "HorIn"}], "+", "offsetRay"}]}]}]}], ";", " ", 
     "\[IndentingNewLine]", "\[IndentingNewLine]", 
     RowBox[{"If", "[", 
      RowBox[{
       RowBox[{"TILT", "\[Equal]", "0"}], ",", 
       RowBox[{"{", 
        RowBox[{"y", ",", 
         RowBox[{"f", "[", "y", "]"}]}], "}"}], ",", 
       RowBox[{"{", 
        RowBox[{
         RowBox[{
          RowBox[{"y", "*", 
           RowBox[{"Cos", "[", "TILT", "]"}]}], "-", 
          RowBox[{
           RowBox[{"f", "[", "y", "]"}], "*", 
           RowBox[{"Sin", "[", "TILT", "]"}]}]}], ",", 
         RowBox[{
          RowBox[{"y", "*", 
           RowBox[{"Sin", "[", "TILT", "]"}]}], "+", 
          RowBox[{
           RowBox[{"f", "[", "y", "]"}], "*", 
           RowBox[{"Cos", "[", "TILT", "]"}]}]}]}], "}"}]}], "]"}]}]}], 
   "]"}]}]], "Input"]
}, Open  ]],

Cell[CellGroupData[{

Cell[TextData[Cell[BoxData[
 RowBox[{"MDHW", "-", "SPS"}]], "Input"]], "Section",
 Background->RGBColor[1, 1, 0]],

Cell[BoxData[
 RowBox[{
  RowBox[{"MDHW", "[", 
   RowBox[{"y_", ",", "TILT_"}], "]"}], ":=", 
  RowBox[{"Module", "[", 
   RowBox[{
    RowBox[{"{", 
     RowBox[{
     "f", ",", "x", ",", "x1", ",", "x2", ",", "C1", ",", "C2", ",", "R1", 
      ",", "R2", ",", "y1", ",", "y2", ",", "y3", ",", "y4", ",", "a", ",", 
      "b", ",", "EX", ",", "TestR", ",", "offsetRay"}], "}"}], ",", 
    "\[IndentingNewLine]", "\[IndentingNewLine]", 
    RowBox[{
     RowBox[{"C1", "   ", "=", " ", 
      RowBox[{"{", 
       RowBox[{"60", ",", " ", "0"}], " ", "}"}]}], ";", 
     "                     ", 
     StyleBox[
      RowBox[{"(*", "  ", 
       RowBox[{"[", "mm", "]"}], "   ", "*)"}],
      FontColor->RGBColor[0, 0, 1]], "\[IndentingNewLine]", 
     RowBox[{"C2", "   ", "=", " ", 
      RowBox[{"{", 
       RowBox[{"58", ",", " ", 
        RowBox[{
         RowBox[{"48.5", "/", "2"}], "-", "10"}]}], "}"}]}], ";", "      ", 
     StyleBox[
      RowBox[{"(*", "  ", 
       RowBox[{"[", "mm", "]"}], "   ", "*)"}],
      FontColor->RGBColor[0, 0, 1]], 
     StyleBox["\[IndentingNewLine]",
      FontColor->RGBColor[0, 0, 1]], 
     StyleBox["\[IndentingNewLine]",
      FontColor->RGBColor[0, 0, 1]], 
     StyleBox[
      RowBox[{"R1", "=", "10"}],
      FontColor->RGBColor[0, 0, 1]], 
     StyleBox[";",
      FontColor->RGBColor[0, 0, 1]], 
     StyleBox["\[IndentingNewLine]",
      FontColor->RGBColor[0, 0, 1]], 
     StyleBox[
      RowBox[{"R2", "=", "10"}],
      FontColor->RGBColor[0, 0, 1]], 
     StyleBox[";",
      FontColor->RGBColor[0, 0, 1]], "\[IndentingNewLine]", 
     "\[IndentingNewLine]", "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"y1", "[", "x_", "]"}], "=", 
      RowBox[{
       SqrtBox[
        RowBox[{
         RowBox[{"R1", "^", "2"}], "-", 
         RowBox[{
          RowBox[{"(", 
           RowBox[{"x", "-", 
            RowBox[{"C1", "[", 
             RowBox[{"[", "1", "]"}], "]"}]}], ")"}], "^", "2"}]}]], "+", 
       RowBox[{"C1", "[", 
        RowBox[{"[", "2", "]"}], "]"}]}]}], ";", "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"y2", "[", "x_", "]"}], "=", 
      RowBox[{
       SqrtBox[
        RowBox[{
         RowBox[{"R2", "^", "2"}], "-", 
         RowBox[{
          RowBox[{"(", 
           RowBox[{"x", "-", 
            RowBox[{"C2", "[", 
             RowBox[{"[", "1", "]"}], "]"}]}], ")"}], "^", "2"}]}]], "+", 
       RowBox[{"C2", "[", 
        RowBox[{"[", "2", "]"}], "]"}]}]}], ";", "\[IndentingNewLine]", 
     "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"y3", "[", "x_", "]"}], "=", 
      RowBox[{
       RowBox[{"a", "*", "x"}], "+", "b"}]}], ";", "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"y4", "[", "x_", "]"}], "=", 
      RowBox[{
       RowBox[{"y2", "'"}], "[", "x", "]"}]}], ";", "\[IndentingNewLine]", 
     "\[IndentingNewLine]", 
     RowBox[{"Off", "[", 
      RowBox[{"FindMinimum", "::", "\"\<lstol\>\""}], "]"}], ";", 
     RowBox[{"EX", "=", 
      RowBox[{"FindMinimum", "[", 
       RowBox[{
        RowBox[{
         RowBox[{"(", 
          RowBox[{
           RowBox[{"y1", "[", 
            RowBox[{"x2", "+", "2"}], "]"}], "-", 
           RowBox[{"(", 
            RowBox[{
             RowBox[{"y2", "[", "x2", "]"}], "+", 
             RowBox[{
              RowBox[{"y4", "[", "x2", "]"}], "*", 
              RowBox[{"(", "2", ")"}]}]}], ")"}]}], ")"}], "*", 
         RowBox[{"Conjugate", "[", 
          RowBox[{"(", 
           RowBox[{
            RowBox[{"y1", "[", 
             RowBox[{"x2", "+", "2"}], "]"}], "-", 
            RowBox[{"(", 
             RowBox[{
              RowBox[{"y2", "[", "x2", "]"}], "+", 
              RowBox[{
               RowBox[{"y4", "[", "x2", "]"}], "*", 
               RowBox[{"(", "2", ")"}]}]}], ")"}]}], ")"}], "]"}]}], ",", 
        RowBox[{"{", 
         RowBox[{"{", 
          RowBox[{"x2", ",", "67", ",", "58.0001", ",", "67.9999"}], "}"}], 
         "}"}], ",", 
        RowBox[{"MaxIterations", "\[Rule]", "20"}]}], "]"}]}], ";", 
     "\[IndentingNewLine]", 
     RowBox[{"On", "[", 
      RowBox[{"FindMinimum", "::", "\"\<lstol\>\""}], "]"}], ";", 
     "\[IndentingNewLine]", "\[IndentingNewLine]", "\[IndentingNewLine]", 
     RowBox[{"x2", "=", 
      RowBox[{"x2", "/.", 
       RowBox[{"EX", "[", 
        RowBox[{"[", "2", "]"}], "]"}]}]}], ";", "\[IndentingNewLine]", 
     RowBox[{"x1", "=", 
      RowBox[{"x2", "+", "2"}]}], ";", "\[IndentingNewLine]", 
     RowBox[{"a", "=", 
      RowBox[{"y4", "[", "x2", "]"}]}], ";", "\[IndentingNewLine]", 
     RowBox[{"b", "=", 
      RowBox[{
       RowBox[{"y2", "[", "x2", "]"}], "-", 
       RowBox[{"a", "*", "x2"}]}]}], ";", "\[IndentingNewLine]", 
     "\[IndentingNewLine]", "\[IndentingNewLine]", 
     RowBox[{"If", "[", 
      RowBox[{
       RowBox[{
        RowBox[{"EX", "[", 
         RowBox[{"[", "1", "]"}], "]"}], ">", "5.0"}], " ", 
       RowBox[{"(*", " ", "mm", " ", "*)"}], ",", "\[IndentingNewLine]", 
       RowBox[{
        RowBox[{"Print", "[", "\"\<MDHW. Error. \>\"", "]"}], ";", 
        "\[IndentingNewLine]", 
        RowBox[{"Print", "[", 
         RowBox[{"\"\<Cannot find intersection between: y1[x]=\>\"", ",", 
          RowBox[{"y1", "[", "x", "]"}], ",", "\"\< and y3[x]=\>\"", ",", 
          RowBox[{"y3", "[", "x", "]"}]}], "]"}], ";", "\[IndentingNewLine]", 
        
        RowBox[{"Print", "[", 
         RowBox[{"\"\<                                  y2[x]=\>\"", ",", 
          RowBox[{"y2", "[", "x", "]"}], ",", "\"\< and y3[x]=\>\"", ",", 
          RowBox[{"y3", "[", "x", "]"}]}], "]"}], ";", "\[IndentingNewLine]", 
        
        RowBox[{"Print", "[", 
         RowBox[{"\"\<  R1=\>\"", ",", "R1", ",", "\"\< R2=\>\"", ",", "R2"}],
          "]"}], ";", "\[IndentingNewLine]", 
        RowBox[{"Return", "[", 
         RowBox[{"-", "1"}], "]"}], ";"}]}], "\[IndentingNewLine]", "]"}], 
     ";", "\[IndentingNewLine]", "\[IndentingNewLine]", "\[IndentingNewLine]",
      "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{
       RowBox[{"48.5", "/", "2."}], "/;", " ", 
       RowBox[{
        RowBox[{"x", " ", ">", " ", "0"}], " ", "&&", " ", 
        RowBox[{"x", " ", "\[LessEqual]", "  ", "58"}]}]}]}], ";", 
     "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{
       RowBox[{"y2", "[", "x", "]"}], "/;", 
       RowBox[{
        RowBox[{"x", " ", ">", " ", "58"}], " ", "&&", " ", 
        RowBox[{"x", " ", "\[LessEqual]", "  ", "x2"}]}]}]}], ";", 
     "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{
       RowBox[{"y3", "[", "x", "]"}], "/;", 
       RowBox[{
        RowBox[{"x", " ", ">", "x2"}], " ", "&&", " ", 
        RowBox[{"x", " ", "\[LessEqual]", " ", "x1"}]}]}]}], ";", 
     "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{
       RowBox[{"y1", "[", "x", "]"}], "/;", 
       RowBox[{
        RowBox[{"x", " ", ">", " ", "x1"}], " ", "&&", " ", 
        RowBox[{"x", " ", "\[LessEqual]", " ", "70"}]}]}]}], ";", 
     "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{"0", "/;", " ", 
       RowBox[{"x", " ", ">", "70"}]}]}], ";", "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{
       RowBox[{"f", "[", 
        RowBox[{"-", "x"}], "]"}], "/;", " ", 
       RowBox[{"x", " ", "\[LessEqual]", " ", "0"}]}]}], " ", ";", 
     "\[IndentingNewLine]", "\[IndentingNewLine]", 
     RowBox[{"If", "[", 
      RowBox[{
       RowBox[{"TILT", "\[Equal]", "0"}], ",", 
       RowBox[{"{", 
        RowBox[{"y", ",", 
         RowBox[{"f", "[", "y", "]"}]}], "}"}], ",", 
       RowBox[{"{", 
        RowBox[{
         RowBox[{
          RowBox[{"y", "*", 
           RowBox[{"Cos", "[", "TILT", "]"}]}], "-", 
          RowBox[{
           RowBox[{"f", "[", "y", "]"}], "*", 
           RowBox[{"Sin", "[", "TILT", "]"}]}]}], ",", 
         RowBox[{
          RowBox[{"y", "*", 
           RowBox[{"Sin", "[", "TILT", "]"}]}], "+", 
          RowBox[{
           RowBox[{"f", "[", "y", "]"}], "*", 
           RowBox[{"Cos", "[", "TILT", "]"}]}]}]}], "}"}]}], "]"}]}]}], 
   "]"}]}]], "Input",
 CellChangeTimes->{{3.4203757696516285`*^9, 3.420375828965267*^9}, {
   3.420375873387995*^9, 3.420375891310214*^9}, 3.4203760225471087`*^9, {
   3.4203760934859705`*^9, 3.4203763463189497`*^9}, {3.4203763838040447`*^9, 
   3.4203764657118673`*^9}, {3.4203765255723915`*^9, 3.420376552932292*^9}, {
   3.4203766523873262`*^9, 3.4203767178260827`*^9}, {3.4203767818273115`*^9, 
   3.4203767921243844`*^9}, {3.420380735117688*^9, 3.420380809386509*^9}, {
   3.42038090881748*^9, 3.4203809815686684`*^9}, 3.4203810715195684`*^9, {
   3.420381299423149*^9, 3.4203813054067197`*^9}, {3.420381354900067*^9, 
   3.4203813952227716`*^9}, {3.420381441217061*^9, 3.4203817073287296`*^9}, {
   3.420381739512835*^9, 3.420381777165229*^9}, 3.420381877076872*^9, {
   3.4204310433843603`*^9, 3.420431050915851*^9}, {3.4204315073523316`*^9, 
   3.420431518305807*^9}, {3.420431972320335*^9, 3.4204319858988943`*^9}, {
   3.4204320346504545`*^9, 3.420432072854802*^9}, {3.4204357895831084`*^9, 
   3.420435869632545*^9}, {3.420439495686075*^9, 3.4204395381093073`*^9}, {
   3.4204396028613796`*^9, 3.420439609752225*^9}, {3.420439749631701*^9, 
   3.4204397640540376`*^9}}],

Cell[CellGroupData[{

Cell[BoxData[
 RowBox[{"{", 
  RowBox[{"64", ",", " ", 
   RowBox[{
    RowBox[{
     RowBox[{"(", 
      RowBox[{"42.2", "-", "4"}], ")"}], "/", "2"}], "-", "11"}]}], 
  "}"}]], "Input",
 CellChangeTimes->{{3.4788686190045033`*^9, 3.4788686226605897`*^9}}],

Cell[BoxData[
 RowBox[{"{", 
  RowBox[{"64", ",", "8.100000000000001`"}], "}"}]], "Output",
 CellChangeTimes->{3.4788686234886775`*^9, 3.478869560477948*^9, 
  3.4788709848074336`*^9}]
}, Open  ]],

Cell[CellGroupData[{

Cell[BoxData[
 RowBox[{"{", 
  RowBox[{"0", ",", " ", 
   RowBox[{
    RowBox[{
     RowBox[{"(", 
      RowBox[{"42.2", "-", "4"}], ")"}], "/", "2"}], "-", "698"}]}], 
  "}"}]], "Input",
 CellChangeTimes->{3.478942905268579*^9}],

Cell[BoxData[
 RowBox[{"{", 
  RowBox[{"0", ",", 
   RowBox[{"-", "678.9`"}]}], "}"}]], "Output",
 CellChangeTimes->{3.47894290570604*^9}]
}, Open  ]]
}, Open  ]],

Cell[CellGroupData[{

Cell[TextData[Cell[BoxData[
 RowBox[{"MBA", "-", "SPS"}]], "Input"]], "Section",
 CellChangeTimes->{{3.478859023780221*^9, 3.478859028217636*^9}},
 Background->RGBColor[1, 1, 0]],

Cell[BoxData[
 RowBox[{
  RowBox[{"MBA", "[", 
   RowBox[{"y_", ",", "TILT_"}], "]"}], ":=", 
  RowBox[{"Module", "[", 
   RowBox[{
    RowBox[{"{", 
     RowBox[{
     "f", ",", "x", ",", "x1", ",", "x2", ",", "C1", ",", "C2", ",", "C3", 
      ",", "R1", ",", "R2", ",", "R3", ",", "y1", ",", "y2", ",", "y3", ",", 
      "a", ",", "b", ",", "EX", ",", "TestR", ",", "offsetRay"}], "}"}], ",", 
    "\[IndentingNewLine]", "\[IndentingNewLine]", 
    RowBox[{
     RowBox[{"C1", "   ", "=", " ", 
      RowBox[{"{", 
       RowBox[{"0", ",", " ", "0"}], " ", "}"}]}], ";", 
     "                                                                        \
     ", 
     StyleBox[
      RowBox[{"(*", "  ", 
       RowBox[{"[", "mm", "]"}], "   ", "*)"}],
      FontColor->RGBColor[0, 0, 1]], "\[IndentingNewLine]", 
     RowBox[{"C2", "   ", "=", " ", 
      RowBox[{"{", 
       RowBox[{"0", ",", " ", 
        RowBox[{"-", "678.9"}]}], "}"}]}], ";", 
     "                                                                  ", 
     StyleBox[
      RowBox[{"(*", "  ", 
       RowBox[{"[", "mm", "]"}], "   ", "*)"}],
      FontColor->RGBColor[0, 0, 1]], 
     StyleBox["\[IndentingNewLine]",
      FontColor->RGBColor[0, 0, 1]], 
     RowBox[{"C3", "   ", "=", " ", 
      RowBox[{"{", 
       RowBox[{"64.18985995702228", ",", " ", "8.108256394818845"}], "}"}]}], 
     ";", "    ", 
     RowBox[{"(*", "  ", 
      StyleBox[
       RowBox[{"[", "mm", "]"}],
       FontColor->RGBColor[0, 0, 1]], 
      StyleBox["   ",
       FontColor->RGBColor[0, 0, 1]], 
      StyleBox["*)",
       FontColor->RGBColor[0, 0, 1]]}], 
     StyleBox["\[IndentingNewLine]",
      FontColor->RGBColor[0, 0, 1]], 
     StyleBox["\[IndentingNewLine]",
      FontColor->RGBColor[0, 0, 1]], 
     StyleBox["\[IndentingNewLine]",
      FontColor->RGBColor[0, 0, 1]], 
     StyleBox["\[IndentingNewLine]",
      FontColor->RGBColor[0, 0, 1]], 
     StyleBox[
      RowBox[{"R1", "=", "72.7"}],
      FontColor->RGBColor[0, 0, 1]], 
     StyleBox[";",
      FontColor->RGBColor[0, 0, 1]], 
     StyleBox["\[IndentingNewLine]",
      FontColor->RGBColor[0, 0, 1]], 
     StyleBox[
      RowBox[{"R2", "=", "698"}],
      FontColor->RGBColor[0, 0, 1]], 
     StyleBox[";",
      FontColor->RGBColor[0, 0, 1]], "\[IndentingNewLine]", 
     RowBox[{"R3", "=", "8"}], ";", "\[IndentingNewLine]", 
     "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"y1", "[", "x_", "]"}], "=", 
      RowBox[{
       SqrtBox[
        RowBox[{
         RowBox[{"R1", "^", "2"}], "-", 
         RowBox[{
          RowBox[{"(", 
           RowBox[{"x", "-", 
            RowBox[{"C1", "[", 
             RowBox[{"[", "1", "]"}], "]"}]}], ")"}], "^", "2"}]}]], "+", 
       RowBox[{"C1", "[", 
        RowBox[{"[", "2", "]"}], "]"}]}]}], ";", "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"y2", "[", "x_", "]"}], "=", 
      RowBox[{
       SqrtBox[
        RowBox[{
         RowBox[{"R2", "^", "2"}], "-", 
         RowBox[{
          RowBox[{"(", 
           RowBox[{"x", "-", 
            RowBox[{"C2", "[", 
             RowBox[{"[", "1", "]"}], "]"}]}], ")"}], "^", "2"}]}]], "+", 
       RowBox[{"C2", "[", 
        RowBox[{"[", "2", "]"}], "]"}]}]}], ";", "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"y3", "[", "x_", "]"}], "=", 
      RowBox[{
       SqrtBox[
        RowBox[{
         RowBox[{"R3", "^", "2"}], "-", 
         RowBox[{
          RowBox[{"(", 
           RowBox[{"x", "-", 
            RowBox[{"C3", "[", 
             RowBox[{"[", "1", "]"}], "]"}]}], ")"}], "^", "2"}]}]], "+", 
       RowBox[{"C3", "[", 
        RowBox[{"[", "2", "]"}], "]"}]}]}], ";", "\[IndentingNewLine]", 
     "\[IndentingNewLine]", 
     RowBox[{"(*", "\[IndentingNewLine]", 
      RowBox[{
       RowBox[{"Off", "[", 
        RowBox[{"FindMinimum", "::", "\"\<lstol\>\""}], "]"}], ";", 
       RowBox[{"EX", "=", 
        RowBox[{"FindMinimum", "[", 
         RowBox[{
          RowBox[{
           RowBox[{
            RowBox[{"(", 
             RowBox[{
              RowBox[{"y2", "[", "x1", "]"}], "-", 
              RowBox[{"y3", "[", "x1", "]"}]}], ")"}], "*", 
            RowBox[{"Conjugate", "[", 
             RowBox[{"(", 
              RowBox[{
               RowBox[{"y2", "[", "x1", "]"}], "-", 
               RowBox[{"y3", "[", "x1", "]"}]}], ")"}], "]"}]}], "+", 
           RowBox[{
            RowBox[{"(", 
             RowBox[{
              RowBox[{"y1", "[", "x2", "]"}], "-", 
              RowBox[{"y3", "[", "x2", "]"}]}], ")"}], "*", 
            RowBox[{"Conjugate", "[", 
             RowBox[{"(", 
              RowBox[{
               RowBox[{"y1", "[", "x2", "]"}], "-", 
               RowBox[{"y3", "[", "x2", "]"}]}], ")"}], "]"}]}]}], ",", 
          RowBox[{"{", 
           RowBox[{
            RowBox[{"{", 
             RowBox[{"x1", ",", "75"}], "}"}], ",", 
            RowBox[{"{", 
             RowBox[{"x2", ",", "64"}], "}"}]}], "}"}], ",", 
          RowBox[{"MaxIterations", "\[Rule]", "50"}]}], "]"}]}], ";", 
       "\[IndentingNewLine]", 
       RowBox[{"On", "[", 
        RowBox[{"FindMinimum", "::", "\"\<lstol\>\""}], "]"}], ";", 
       "\[IndentingNewLine]", "\[IndentingNewLine]", "\[IndentingNewLine]", 
       RowBox[{"x1", "=", 
        RowBox[{"x1", "/.", 
         RowBox[{"EX", "[", 
          RowBox[{"[", "2", "]"}], "]"}]}]}], ";", "\[IndentingNewLine]", 
       RowBox[{"x2", "=", 
        RowBox[{"x2", "/.", 
         RowBox[{"EX", "[", 
          RowBox[{"[", "2", "]"}], "]"}]}]}], ";", "\[IndentingNewLine]", 
       "\[IndentingNewLine]", "\[IndentingNewLine]", 
       RowBox[{"If", "[", 
        RowBox[{
         RowBox[{
          RowBox[{"EX", "[", 
           RowBox[{"[", "1", "]"}], "]"}], ">", "0.0"}], " ", 
         RowBox[{"(*", " ", "mm", " ", "*)"}], ",", "\[IndentingNewLine]", 
         RowBox[{
          RowBox[{"Print", "[", "\"\<MBA. Error. \>\"", "]"}], ";", 
          "\[IndentingNewLine]", 
          RowBox[{"Print", "[", 
           RowBox[{"\"\<Cannot find intersection between: y1[x]=\>\"", ",", 
            RowBox[{"y1", "[", "x", "]"}], ",", "\"\< and y3[x]=\>\"", ",", 
            RowBox[{"y3", "[", "x", "]"}]}], "]"}], ";", 
          "\[IndentingNewLine]", 
          RowBox[{"Print", "[", 
           RowBox[{"\"\<                                  y2[x]=\>\"", ",", 
            RowBox[{"y2", "[", "x", "]"}], ",", "\"\< and y3[x]=\>\"", ",", 
            RowBox[{"y3", "[", "x", "]"}]}], "]"}], ";", 
          "\[IndentingNewLine]", 
          RowBox[{"Print", "[", 
           RowBox[{
           "\"\<  x1=\>\"", ",", "x1", ",", "\"\< x2=\>\"", ",", "x2"}], 
           "]"}], ";", "\[IndentingNewLine]", 
          RowBox[{"Print", "[", 
           RowBox[{
           "\"\<  R1=\>\"", ",", "R1", ",", "\"\< R2=\>\"", ",", "R2"}], 
           "]"}], ";", "\[IndentingNewLine]", 
          RowBox[{"Abort", "[", "]"}], ";"}]}], "\[IndentingNewLine]", 
        RowBox[{"(*", " ", 
         RowBox[{
          RowBox[{"Return", "[", 
           RowBox[{"-", "1"}], "]"}], ";"}], " ", "*)"}], 
        "\[IndentingNewLine]", "]"}], ";"}], "\[IndentingNewLine]", 
      "\[IndentingNewLine]", "*)"}], "\[IndentingNewLine]", 
     "\[IndentingNewLine]", 
     RowBox[{"x1", "=", "64.84496415331645"}], ";", "\[IndentingNewLine]", 
     RowBox[{"x2", "=", "72.12678182553574"}], ";", "\[IndentingNewLine]", 
     "\[IndentingNewLine]", "\[IndentingNewLine]", "\[IndentingNewLine]", 
     "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{
       RowBox[{"y2", "[", "x", "]"}], "/;", 
       RowBox[{
        RowBox[{"x", " ", ">", " ", "0"}], " ", "&&", " ", 
        RowBox[{"x", " ", "\[LessEqual]", "  ", "x1"}]}]}]}], ";", 
     "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{
       RowBox[{"y3", "[", "x", "]"}], "/;", 
       RowBox[{
        RowBox[{"x", " ", ">", "x1"}], " ", "&&", " ", 
        RowBox[{"x", " ", "\[LessEqual]", " ", "x2"}]}]}]}], ";", 
     "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{
       RowBox[{"y1", "[", "x", "]"}], "/;", 
       RowBox[{
        RowBox[{"x", " ", ">", " ", "x2"}], " ", "&&", " ", 
        RowBox[{"x", " ", "\[LessEqual]", " ", "72.7"}]}]}]}], ";", 
     "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{"0", "/;", " ", 
       RowBox[{"x", " ", ">", "72.7"}]}]}], ";", "\[IndentingNewLine]", 
     RowBox[{
      RowBox[{"f", "[", "x_", "]"}], ":=", 
      RowBox[{
       RowBox[{"f", "[", 
        RowBox[{"-", "x"}], "]"}], "/;", " ", 
       RowBox[{"x", " ", "\[LessEqual]", " ", "0"}]}]}], " ", ";", 
     "\[IndentingNewLine]", 
     RowBox[{"If", "[", 
      RowBox[{
       RowBox[{"TILT", "\[Equal]", "0"}], ",", 
       RowBox[{"{", 
        RowBox[{"y", ",", 
         RowBox[{"f", "[", "y", "]"}]}], "}"}], ",", 
       RowBox[{"{", 
        RowBox[{
         RowBox[{
          RowBox[{"y", "*", 
           RowBox[{"Cos", "[", "TILT", "]"}]}], "-", 
          RowBox[{
           RowBox[{"f", "[", "y", "]"}], "*", 
           RowBox[{"Sin", "[", "TILT", "]"}]}]}], ",", 
         RowBox[{
          RowBox[{"y", "*", 
           RowBox[{"Sin", "[", "TILT", "]"}]}], "+", 
          RowBox[{
           RowBox[{"f", "[", "y", "]"}], "*", 
           RowBox[{"Cos", "[", "TILT", "]"}]}]}]}], "}"}]}], "]"}]}]}], 
   "]"}]}]], "Input",
 CellChangeTimes->{{3.4203757696516285`*^9, 3.420375828965267*^9}, {
   3.420375873387995*^9, 3.420375891310214*^9}, 3.4203760225471087`*^9, {
   3.4203760934859705`*^9, 3.4203763463189497`*^9}, {3.4203763838040447`*^9, 
   3.4203764657118673`*^9}, {3.4203765255723915`*^9, 3.420376552932292*^9}, {
   3.4203766523873262`*^9, 3.4203767178260827`*^9}, {3.4203767818273115`*^9, 
   3.4203767921243844`*^9}, {3.420380735117688*^9, 3.420380809386509*^9}, {
   3.42038090881748*^9, 3.4203809815686684`*^9}, 3.4203810715195684`*^9, {
   3.420381299423149*^9, 3.4203813054067197`*^9}, {3.420381354900067*^9, 
   3.4203813952227716`*^9}, {3.420381441217061*^9, 3.4203817073287296`*^9}, {
   3.420381739512835*^9, 3.420381777165229*^9}, 3.420381877076872*^9, {
   3.4204310433843603`*^9, 3.420431050915851*^9}, {3.4204315073523316`*^9, 
   3.420431518305807*^9}, {3.420431972320335*^9, 3.4204319858988943`*^9}, {
   3.4204320346504545`*^9, 3.420432072854802*^9}, {3.4204357895831084`*^9, 
   3.420435869632545*^9}, {3.420439495686075*^9, 3.4204395381093073`*^9}, {
   3.4204396028613796`*^9, 3.420439609752225*^9}, {3.420439749631701*^9, 
   3.4204397640540376`*^9}, {3.478859157605777*^9, 3.4788591602932253`*^9}, {
   3.4788592281044235`*^9, 3.4788593172902107`*^9}, {3.4788594342879643`*^9, 
   3.4788594650998726`*^9}, {3.478859568894755*^9, 3.47885957905081*^9}, {
   3.4788596364090834`*^9, 3.47885964547141*^9}, {3.4788603143960657`*^9, 
   3.478860331692609*^9}, {3.4788603720668335`*^9, 3.478860386738427*^9}, {
   3.47886366320234*^9, 3.478863731670936*^9}, {3.478864066050488*^9, 
   3.478864193792083*^9}, {3.478864265444664*^9, 3.4788642930994983`*^9}, {
   3.4788644067811775`*^9, 3.4788644247336016`*^9}, {3.4788644746379356`*^9, 
   3.4788644888248906`*^9}, {3.478864835468647*^9, 3.478864847624508*^9}, {
   3.4788649167629204`*^9, 3.4788649218408833`*^9}, 3.478864966058218*^9, {
   3.4788650133223667`*^9, 3.478865044134078*^9}, {3.4788650806018944`*^9, 
   3.478865146334587*^9}, {3.47886528058115*^9, 3.4788652815498753`*^9}, {
   3.478865334751638*^9, 3.4788653459388514`*^9}, {3.478865444170712*^9, 
   3.4788654465925245`*^9}, {3.4788657133860283`*^9, 
   3.4788657141981487`*^9}, {3.478865759833068*^9, 3.478865791943059*^9}, {
   3.4788658450122094`*^9, 3.47886584584017*^9}, {3.4788658803333254`*^9, 
   3.478865880552032*^9}, {3.4788659222781267`*^9, 3.47886592271554*^9}, {
   3.47886598643727*^9, 3.4788659895147843`*^9}, {3.4788661138807306`*^9, 
   3.4788661143650093`*^9}, {3.478866257800581*^9, 3.478866265659151*^9}, {
   3.478866419815239*^9, 3.47886661338004*^9}, {3.47886813551054*^9, 
   3.478868136916727*^9}, {3.478868229662572*^9, 3.478868246318075*^9}, {
   3.478868336767148*^9, 3.47886833750149*^9}, {3.478868384108777*^9, 
   3.4788683847337494`*^9}, {3.4788684656207504`*^9, 3.478868466355092*^9}, {
   3.47886850257222*^9, 3.47886853080533*^9}, {3.4788685786000633`*^9, 
   3.4788685787563066`*^9}, {3.4788686304883637`*^9, 3.478868686454606*^9}, {
   3.4788687369679685`*^9, 3.4788688966483145`*^9}, {3.478869134950138*^9, 
   3.4788691467464848`*^9}, {3.4788692178995466`*^9, 
   3.4788692977865925`*^9}, {3.478869364267989*^9, 3.4788693644554806`*^9}, {
   3.478869400531989*^9, 3.4788694224685063`*^9}, {3.4788695513533573`*^9, 
   3.478869580352058*^9}, {3.478869736054016*^9, 3.478869736755625*^9}, {
   3.478869876204212*^9, 3.478869879836985*^9}, 3.478870544307565*^9, {
   3.4788707290833983`*^9, 3.478870734254247*^9}, {3.478870835109234*^9, 
   3.47887085490302*^9}, {3.478870945656446*^9, 3.478870955795708*^9}, {
   3.478871061078431*^9, 3.4788710614690037`*^9}, {3.478871093761538*^9, 
   3.4788710943083396`*^9}, {3.4788712595696383`*^9, 3.478871260397668*^9}, {
   3.4788713104544*^9, 3.478871310829357*^9}, {3.478871415161087*^9, 
   3.478871423941325*^9}, {3.478871477185418*^9, 3.4788714976831875`*^9}, {
   3.478871584439372*^9, 3.4788716311061697`*^9}, {3.47887166689915*^9, 
   3.4788716865376377`*^9}, {3.4788717221275153`*^9, 3.478871725595888*^9}, {
   3.478942915033329*^9, 3.478942956795212*^9}}]
}, Open  ]]
}, Open  ]]
}, Closed]],

Cell[CellGroupData[{

Cell["SPS", "Title",
 CellChangeTimes->{3.4204398284623485`*^9},
 Background->RGBColor[0, 1, 0]],

Cell[BoxData[" "], "Input",
 CellChangeTimes->{3.636377485296435*^9}]
}, Closed]],

Cell[CellGroupData[{

Cell[TextData[StyleBox["MBA",
 FontFamily->"Courier"]], "Title",
 CellChangeTimes->{
  3.4204398284623485`*^9, {3.4788651743494945`*^9, 3.4788651758025827`*^9}},
 Background->RGBColor[1, 1, 0]],

Cell[BoxData[
 RowBox[{"Clear", "[", 
  RowBox[{"APER1", ",", "APER2", ",", "APER3", ",", "APER4", ",", "TILT"}], 
  "]"}]], "Input",
 CellChangeTimes->{3.4204398284623485`*^9}],

Cell[BoxData[
 RowBox[{
  RowBox[{"APER1", "=", "70"}], ";", 
  RowBox[{"APER2", "=", "24.5"}], ";", 
  RowBox[{"APER3", "=", "70"}], ";", 
  RowBox[{"APER4", "=", "57"}], ";", 
  RowBox[{"TILT", "=", "0"}], ";"}]], "Input",
 CellChangeTimes->{
  3.4204398284623485`*^9, {3.420439961747864*^9, 3.4204399678261833`*^9}, {
   3.420440017827783*^9, 3.420440020812254*^9}}],

Cell[CellGroupData[{

Cell[BoxData[
 RowBox[{"Show", "[", "\[IndentingNewLine]", 
  RowBox[{"ParametricPlot", "[", 
   RowBox[{
    RowBox[{"{", 
     RowBox[{
      RowBox[{"MBA", "[", 
       RowBox[{"x", ",", "0"}], "]"}], ",", 
      RowBox[{"-", 
       RowBox[{"MBA", "[", 
        RowBox[{"x", ",", "0"}], "]"}]}]}], "}"}], ",", 
    RowBox[{"{", 
     RowBox[{"x", ",", 
      RowBox[{"-", "90"}], ",", "90"}], "}"}], ",", 
    RowBox[{"PlotRange", "\[Rule]", 
     RowBox[{"{", 
      RowBox[{
       RowBox[{"{", 
        RowBox[{
         RowBox[{"-", "90"}], ",", "90"}], "}"}], ",", 
       RowBox[{"{", 
        RowBox[{
         RowBox[{"-", "30"}], ",", "30"}], "}"}]}], "}"}]}], ",", 
    RowBox[{"AspectRatio", "\[Rule]", "Automatic"}], ",", 
    RowBox[{"PlotStyle", "\[Rule]", 
     RowBox[{"{", 
      RowBox[{
       RowBox[{"{", 
        RowBox[{"RGBColor", "[", 
         RowBox[{"1", ",", "0", ",", "0"}], "]"}], "}"}], ",", 
       RowBox[{"{", 
        RowBox[{"RGBColor", "[", 
         RowBox[{"1", ",", "0", ",", "0"}], "]"}], "}"}], ",", 
       RowBox[{"{", 
        RowBox[{"RGBColor", "[", 
         RowBox[{"0", ",", "0", ",", "1"}], "]"}], "}"}], ",", 
       RowBox[{"{", 
        RowBox[{"RGBColor", "[", 
         RowBox[{"0", ",", "0", ",", "1"}], "]"}], "}"}]}], "}"}]}]}], "]"}], 
  "\[IndentingNewLine]", "]"}]], "Input",
 CellChangeTimes->{{3.4203819344616203`*^9, 3.420381955740691*^9}, 
   3.4203821089911737`*^9, 3.4204397902111244`*^9, 3.4204398284623485`*^9, 
   3.420439872760641*^9, 3.420439907480502*^9, {3.42044005631339*^9, 
   3.4204400695013113`*^9}, {3.4731602638346443`*^9, 3.473160265475185*^9}, {
   3.4731603920624533`*^9, 3.4731604077179017`*^9}, {3.478865185739828*^9, 
   3.4788652078330126`*^9}, {3.478865526559228*^9, 3.4788655351215086`*^9}}],

Cell[BoxData[
 GraphicsBox[{{}, {}, 
   {RGBColor[1, 0, 0], LineBox[CompressedData["
1:eJxN2HlcTG3YOPDRrn1XKqZd60wzlWzNpSIqdc60WEqmEEKiVcQgyZoKJdtE
Ug+VFEqYW1FpV5EnyWilTSJFye/2+7zvM+/5Z+b7ue5z7uXMOdd9jW7gLvZm
EQqFMjWDQvn7+f8Prg/6368/snSPRO0XenCVo8SXaKFbL8XLduwWOm++nObj
jUKv3zWbEe0s9KMO600j8kKHP9lWJbji/Z8X5E5seZzt9Z+zhytevin3/M/V
d3RMvJHQQ8HhCc2PhWb06To33hf6yYf9z1/eErqpkcF/fFLoqXtXi657Cj1n
95iKLiH0Uppb2DU3oeNv/7S6vExopUyv/PPzhTY6L/1PgpbQHlGR10K62P95
YbVJP++D0EY6762b3wk9XeZYPb9F6Dx5pTHKC6Hlsm67pGQJPTHhf/7FdaG7
XZUF41eFfvw1OsIvVegdS5bzDBOErmkRjD3cJvQD43PQv1no6zHOJ7UDhY6h
5lEPrRPadMc+VxdXodX5lhf2OwstotwpyHMUuu3hikiVxUJXSE+hZXZC31uf
LxNtLfTVu4E+/9CFPi6qntFuLnS4z8sBeRM2uvn4q99XUhI4Ofttlxqykbp8
f+bgaUVwm6IdCtNloxfJy+9vdlMFO4+umps6bLRoedxV/bBZYHD9gvpbTTa6
rPCjWmXBbFAcWxkgrc5G+ic5VW6PtOFT+t0fIfJs9DLVyeH+eSq0DG1cmiHN
Rnbuou/eXNAFBLNONUuwUQqlqfJKnB7cSal+Iy7KRlGHjI/uWKAPab2xunZ/
SHThhUDDqlof4hZY7QieJJEr3LujudwAQk91P7g8TqI1z1pKBgoNwO9D6oyG
byTS/tlbx5llCM4MV7cZIyTq7jUIqdpjCDGHJZPDB0kUh/b1M8oM4U5TeWvf
JxLtOu04/U7WCJTDFm+s/0iimN9Gh/ZfMAKn8onspR0kkhf0qG55YwRRKveH
i9pIlLEpeO5xFWNoL7SIudRMonCNxHfH4o1BXqyfL99IImLLy9Lmx8aw1CtL
/HAtieyW23Us+GoMWd/nJG19QaLZx39c7fWaB6E2itk2D0m0R7uiplXaBK4f
rR3KLiRRtaq2kY2NCbx+ncDUvksimaoXfpH+JrAwcgZfJIdEn88ry3XkmoDY
w9HXDekk0rVYkZqy1BRsJfO1HFNJZJlxQ2bHJlPYtnp7wIMUEp36XBHHjTeF
+vGuwcunSGRtJDEVU2UKaXavRYMPkOhxq9q6bU5mUJ2QtPJ9DIkON/Ul/htg
Br/frkokokjEPx625/4BMwjcWzF7fiiJ1idMpj97YAbmjx5aiQWS6GSbZ2cq
1Rz8pcOjovxJtOjI997mBeaQtI7+pH8diXw9vB+msc3hx6/sFa888fok3v5S
edgcni1K33B1GR6v0csu0Q5z+H7S56aSA4mOjChw67+Zg1G78kCcPYmoopWm
NjMt4NT+k5Hb55MokJ7q28GwAJ8n+0/bmZAof+3ss68OWUC//YbSJlkSldT9
LjyjYAm9+tGDP6VItHsTs8lG1xI6pZJ0dMVJFJk04/NhhiX821R2cNdvAo2T
FkaqXpZQFWTkJDtMINuGA3bWKZbw3JUVwewn0I+9KW/Mr1sCoq/JWtdLIMcx
xRMtdy2h+NdxqZwOArkQdyat6yzh1pmh2mUNBPKUiilgi9DgepjE9I4aAt2s
VOptl6fB1TVzaecqCTT98vQXbS0aXNAjkzr5BAppv+H1jEGD+AdF3gfvEqhx
f2Z9rj8NDl+qi8+6Q6CKb6TDz600OMDtfViXTaDkRW7n/uyhQYSLxmztDAKp
OZcP28fTYFPHvo7iJALpzj9Kv5BDA075OQXBaQKxHuuGVBTQwC87FyRPEGjh
7Wrn+yU08Nzz4br3Ydzfm27fxioauK+eaN5/gED9m1vZvxto4LJYSTwzhkCm
EdIb+t/QwEHCccvoHgIpVspLSnTTwH7AN01zF4H2/epaatNPg4WN4S9hO4HM
Q0waDUdowEjPMkvcSCAxrYg/rpM0sDzI93uwgUB27aC8lEIH001vT7/3JdC9
9PPsJyJ00LWUHjHzItCaYaJhrSQdtFX0dT0JAiVuWLQ0ZiYdNCYWsWPcCFQZ
IeW2X4YOqu+9jmSswOujWyHBkaODYtnOoionAm2XUDpmqEAH2VvxPV+AQL6b
NT/WKtJB6tQ19VlLCFRccMvYR5kOFJ9X0ZttCCTQVplUV6PD1ML+nFNWBKKM
fXGNV6fDxFzRd4UWBOLKNDuNzaLDl8/WS0SMCMSj5lk2zaZDR2zajGvqBOLo
VnYeo9JhvI87760yPv/ylfohXTwe9jYPJQUCUfff2eypT4elRguvHJHE7aMj
zusY0cH5ysPdjSMeCLLLJnPN6NBkby8ILPJAnMelXU9t6fDpkOuTY4s8EK/9
rkGGGx1UpIKiXq10R8A4GL8lig5PH2qGdsa7IUqP36bb5Xi+tbNmfb7igrhK
vnPNlawg/8g5h52vVyDqI9eJLC8rePay2XtQzRkh88cTS5KtIDJ8/awA+jIE
D6jXfjRYwcGyzes9tzsi3vY9Jc/FGGAWUUwu4i5FSO2Bfo0dA07vuOS7eDEL
cYqGD6UFMWCnTbn27+JFiBK9/PalUwxIqTy4MOfzfAQj0evu32XAj7zZrbve
zUeccTUpRgED1l24H2ZbNx/xRvy252FTNw/cKb+L26/5zM66x4A7IqvndkTN
R8iDkpVcxICKJZZiKhI4brHSb30xA34Vttft17NFPAsv6VI+AwJ5CwIIX2vE
Ze8MT61jQH/b8tu9rtaIU+68VbqeAXvUvMb2L7ZGAugRi8U+ciLkeI6ONQK5
YLuABgZkht8oEBEwESf1WoLhKwb0rZATub+JiVDgh7orLQzY8VVwXTOEgVBO
06DbOwZ8NxsezPdnIO6+DT+LsGODJm2XezCQYG9RnnY7A868U6vZQ2cgStpD
lQHs/Bcu32pGrZAg2ajySAcDRi8WOR6IskLUjqrmzI8MiHJI6O7k0hG1X+/o
zT483qRm8We76YgSlv6T8okBIYI5xtcC6YjnIDbbDzvowP1tvk50hBbk+yt9
ZoD3o87hZklszaDxqH4GbNkUM3pch4a4r8KCbIYYIHDs1nJfYIHQ5v5Fu0cZ
8PZjjL+0FvayT5Zl2A0HlTIqpswRx6O9TvkbA56W2huxELbnLYVC7CvMi3S6
M7Zz7fUv3/H903dfpuxthlBpsOTacQY0ixSHvAk1QZwDj6oHJxlAOXnheLqX
CRIcIo9aTjHAXCUi09/OBPGqK3/swo7XZ7T1/pmHUCx7+iv2Qqc7y8bPzEOc
zM5ro78ZwDvK09bINUZo3x/z3j94/lLHq9d+NkTU1/d2XRBlwqWzW3p06gwR
Sl8j0YBdpbGc0nkXx2UEnpJiTNAzEbUNjsZmnlOJwn69MjYjRhL7RIqhpzgT
Fp/cHX3J0ACBz++U3xJMkJZfZ/Q+QA9Rq0fStaSZcGixzmVw1EOCnvCZHtgT
wQKlTAM9hDol9Q5j91YG/Q7u00WoZh3Zh112KKxlYocu4gY+yM6VYcK+sVOH
VaOpCHG9FprKMWFUn5iIWktFXMeGlWuwt7FVQt4tpCKexDrReOw8f2ah0+Rc
BK+uhQuwg5rcAjgScxF35bBHkjwTWksOPknV1kHU3szPnQpMqFCXyPH/oI24
nsbpMopMKAo7dc7wujbioUffmdhnLS5uLzTG8deq2UewV2Tc02xgaCHB4VTJ
uUpMKE7oiZBYqYkERFfOMmUmpK92tYyIUEMcn6/72Kp4vAkB1a6L1RA8LAsP
wXZ9FBWkJ6qGKOvu6J3AntLOvNpwVhXxEqquIOwNnVPypndU8P03VDJVY4LB
zrwvHZ1KiKOxd3AYO/bq85P3c5SQILHJVkKdCW8a2oxPheJ4rZOtDvYxhiRn
wbQi4t0L83LB7h/f0JiiqYhgalIuA9tfXD8wiSeLuNzHETCLCQpbPdLtLWUR
9cxNJU9sVL2vaaBUBglqbgVuxtY/2+KwvFUaUUfG9Y9jf5odrz8pNxPB3kr9
Ouz02Hu+2ZekEDUnZut7bFdBR4q3iRQS2DgHDmHn3ZwvdtdJEkGMeYSsBhPC
6J+7N+0TR9QF8zScsQ1S1HSUZ4ojbluWuDf2m7Gl3vwLYoj6xz47ENuuNP2F
5j1RROkulY3Fnl7mllX/aQZCZz+x87Dzs6M79kXOQNwy5ucSbI7MTXUTsRmI
mpZm/QK7vPF3/JG5FERdkt/fhq300L8h9M4Un9Kg2CKiyYTb5WmFK2on+WAd
1CODvayxKZU6+IvPEePnqWLv/byc02j2kw8jMdsMsVV+cJ2yXSf4oNSxzgI7
V6R0Hnf7OJ9zy0nMBvujFu0r7fYYn7JE+6Aj9r55215L1nznU5aeJlyw1Wxu
lHzo/8aH8hltBPZK91mHE01H+eAyproeu2sdGbTF5StfwA6vCMSO3XLShRU8
wud+/EHbih04449hh+cQn3tBwmwP9oXZYcOnUwb4VJTyOBK7mtn3YEnzZz6K
MJDYhz3t5ntwSPkTn1dcLHkQmxHU4HyF3cunniCeHcYOOuiouCq5m88ZGGDE
Y6enPXw79aqTD+9P+B3Hri8wy7ij9JFPCbCwP4UteoHVXHy9g8+Jam49gx1c
ZbxJQ+8dn6oba5KE3fRLYSwqo5VP3WDKTMFeaDFxtJXawhdYvft+Dvv6BoH6
fF4jn5KeGHIBW9UgycOCVc1Hqc68VOzuhIDdg0vK+QIz0RNp2FvfbTRavbeY
z/EpM7uIregys+WfoUw+d9bRo3/9/ERLcuD6UyzOLtfUvy6pLJG3PFPAovir
Bfz17GmNmvyzfBanq7Pz7/WWzH5cnvayggV/CrX/OuT+QMa/1XUsbkGC/N/+
PbLlQC6oiYV+corPY/dFGObn9r5mcVsXz/47/oOOS+a4b/mXxXHRtk7G1lDy
Pj3c187ikX/Ez2Kv2WV7wNlawEKDPYmnsQ18yu6nfv/Iomg1vjqBPbLYfaiv
qIvFefek5hj2Y/02A7uIHhbFIj82DjtBOsgvwaaPRVHI7ONiU9/G1sx70M+i
HEzrisYefDpTdG/kIIsnnRYRjl188/zCl7bDLK7uJf4u7OySNy1F70ZYMHB7
32Zs+dzLI+2lX1mC9JKhDdjhvEBZ8cujLG5D9ax12HBs2NHb7zuLisZTVmFn
xRRtiF08xuJEq/Qux5YNidl3U/sHC+UyRljYb70kCsfax1mcY/vMrbBD9ebo
XVg/yYIi22WK2HFdT4PKiSkWp94kWQL7YuaG2yOOv1mchZtOTOHnr8wow9rV
9A+L8itvfx/2CbVkfe6+GSDIvrT17/OrGtn5Qn1sBkBvlUIu9tU3jK25ISJA
9V4SyMMuTG2+0xYgCryiSal47HZNNVubFeIg+Fq3fhV2UMzmtzXPsBnWG+yx
R9ruxwQukgBK7EcZGrb4ZR9+oiWuy9WVtihgW85JW9GvOhOgpNygFr+vuHpa
vtc+ygJn0e4nNtjSR7b/tvGVA57FsjBd7HNdpddqW+QAnm1okcXOyfTr/lkp
D9y8rWmd+P26TaXB1nS1IkBllfEJ7OTziihuiTIInjza+BK/v1tf2CkRMdi/
v9flY2v/4ARqPVQG3pqIrvPYWT4FYvfoKsCzW6EYgF06i73yg74qoGSb3d9w
fui+mNK0QFodODWGhBT20zGzsDEHdeBVxB4aUMHrTT5XKdinDtzdstvqsd1n
jnnNG1IHuFu3LgW7ONqnVb1xFnCrO6o0sU+v1mz/dl4TuN2MBg2cv7YWFuzP
r9cEgcfXjeM4vzkouOhsl5wN1NqevNfYExUx/p3Rfx26JQk70LZd0OirhddP
bqM4tq3atZ5cXR2g7lkb9wHnV8Xd8+O3rdMBTlHY/hLsgdoGI8MUHQCy3DQF
mxdH2XpZbA7wgkX+WYYt8z2g/0TfHKCUTTNu4Xwdui15vNCHCtSe7hA/nM+d
VnhPndXWw/uwmWcS8X6hr+Hxbo9F2KY7Pf2wT6w26JNbpwec2bpl87Abg769
OpGqB9SK6EtoJhPWH026FaesDxRaz5JBKSZEltWxo6UMgFLLW8qUZMKtxctz
Nnw3BEq5ohMX74dcnufOmaNiBKDoznTAHnZVO9duZQRc9LZGFNvat/vA2l1G
QBl6PXFUBOfPvYe9PPtxvGuHQ/wM/Lw8ePpnucAYOA4TKZF4/yVtNd/HstYE
56k3NHW8v6tI1NNZ328CUCR3tf4XAw4Py3WflDIFlHuvOB578nb37s9O2GZO
38Z+MmDQKPl05hNToEYfjm2cYECd9tDz2flmQNHy7o34wYCzUjeYkskWwMtI
ljr8lQEyocekRm7T8e9P9vi1Xga4m/57UPQRrtO6+91WYid3m46rV9EB9chV
jfYwQGNtfc+SbhxX1Ot2wjZyUCs/qW0FAjFuYU8XAxxUb8Qan7YCruuvPE28
395b/HTUPwTviw/pabji/Xsf5Ud7Hd0aqFuq7jTj+kBi6+ssJbAGiqnyjkBs
g4aiUG8PawB29esRXF9wroSJvd9pDVyzo9my2G0LvpoN/oPbb6G6Qg0DavcM
xkgb2oCgujIutZIB97o7NZw1bfH4/qkSR7heqGrwQjPsgGLQnPAxnwHBK++U
P0xaBILp36amZxgQkyu6sUSBBVz+2rjzWxmgZ9DV1LdjKUCtauejhQxg1r/Y
FWHlCJxXS20tZRiQoeLvL6e9DNCFXdEhTVbw6H5UlXHvcqC+zH90Ks0KNr+s
d3G+tQKoK3cE2Ppawc7od3N2n3EBzt2s+cdVrIAaty1Ex9sNELSr19fQgW6W
q9Cy1B0oFzvv10TTIZmWMh240h2Q8sMXMbjeHGPuHfpKuAPsq+SaRNLh0eJl
NQocHDdNnzgaRgcn9/fxrgfcgXrg5/DCEDqs2S03XfbIHXiBzB/nNtLh0MOd
gwVMD+CNzNs+050O3aWe72ARdtvxj7m4vl2OFlQ3OHgAR3qWKNsV17MvxbOH
SBxfUuR8cQUdLrRd2WgS6gGU6YE3+o50+Od3XRvvjgdQXwlkTezo8Fk3tbtS
mQDKsTXN33D93WI0I8BdnQCBiDT/Jq7Pn5ptf9+iSQAI2jmr59LhnA3rzUcq
bq/WU1GiTQf7lX2Vk5YEUB+Gae/D9f48d9LpMIMAzlmDElN1XH97liIpWwJ4
Yd9k2lTpML3acEniAgLWDRy9m6mC63W/xBK1JQRE5xbn/v1/oSngp81lIGBw
9EjUF0U6PAnaeE/PiYCvaWcpuxTw+obOv01zJUBP31RdT5YO+yMyjB+4E/BK
XfOItzQdtsTIZC5mEyAbJxm6S4oOi+M+XF65Fvc3N+KgjxgdjI+v1Gz0IyDG
nxqjL0IH5TOF5304BET22brk/qFBX+qxMxu3EPDYRTygY4wGTZe/SvcHE+Aa
1IiyR2jwOMP3WGgIAePhcnz7ARok36ZxYyMIeDcdWVr7gQaL+a27U48QIN02
Yh5cQQOj50uHdY4R0K+gOvMknwZKL28HZ54g4EJOwqmIYhr0Nh3cWJBEwNEq
Rb+sHBok9Rp711wjQPGHASvkOA32DyS9Im/g9bn643gzlwZBI5Or3mYR0PAy
oOVPFO7vV8PynlwCTrEqW29vxteTi7b7U0rA3LV9H5bZ06BRubPoKJ+A1vUO
R1uZNJxv3KxkywkwCv6aY25Cg7O6VFPNagK8/jXePFeFBgttqrSYbwmQfHPU
fVa3JST6afwJ+k7A4tHQ+Bd7LeFureHZBRMEDL++5C8TbAlNi5m6slMEXHc6
lfh7rSWo6rg7FoiSoH3TPqrTzhLS3x85NqlMwouEc+anRi2gdFWSRr06CRbf
gj4oCyyg/cnVHN5sElyHvK4uqrOAuVdLapbpkaASmSKzM8sCMv2/KJy1ImFs
zW8fqpcFVNRP8QJtSNA7/OBIgr0F9NlLM2wWkBC/VHxb3DwLMJ1r6NUGJDx9
kZRkOWkO+R/WpRkQJMx5uDFD6pI5POJUUEtCSFj8LF3CscwM3jU2F5zcQ8Jl
qyiLi5lmMAUfHfwj8fmhRm/c482ApTu1SfQACb/PzPxZ7mwGzz9a5aw6TYJd
3LAcvcwUeknWQmoSCUYqG1M6rpqCZJlbzeg5ElK/lEcVx5iCy/UtQ6mXSZDz
tRevpplCQ+AVq87bJBwoD180/4wJjDT9U1aUT0LBzCGbWRtNQNmx2PNYIQms
yZnXka0JeOk3R5iXkhD4MSnRoG0eRKYIJP48JcGgzexrYc48SBUdTn1VRoLW
h8Rn96PmQVuX1KPIahJKBxxG0+TnwaSnuuvKehKa9u69yWw1Bu3n+u1aTSR8
m6aeLrhiDBsy7afRvyQ43L0Se1jfGLiqbokp70kY3Q9MdqcRXI9bSw36SEKL
/Z2siStG0L0p3EHmMwm0Hsd0SWkj4LdGv708SML9P0raL58aQrpLbIjlCAk9
IvJ6hSGGEP7kkBj6RoKIyvttrRqG4EGPTyfH8Xy3TIkMlRqA6Y0T9K5fJPB+
vm9V9zEAMfXEivBpEhD5IC20Wx8+JKT4SYiwQX3peguJQH14NJk6mirOBjkt
J/2Pz/XgXMjlBJOZbDjt0EI3+aELuz7y5pTKsqGgtValSFoXXLxuFrkpsgHO
rXqbqkQFg8oclw4VNpxccWrQV3EO/FmQJ9g1iw17xSdXZb7WgrY79yJnaLFh
+qrJ9ImtmlA096Fsyhw27Nx9Y+VosTokJpdeN9BjA0XJ4Xz+bRUIFkd2DwzZ
cDEjnZYjowhO0c/rnU3YUD73Wq/EVQmYO1C16V9z3P5/jl/r634F04VuaXx1
doopdL7jG6Mz84XeZPKBXWAvNOty1ycHB6FnK3w60LJM6IbvI/+Muwm9EImI
2vsKrcqUvNjgL/SXmzK0gEChM0+q+sZtE1phtVFhdZTQ3UMrN64+J3SiVlJ5
aJ3QbjMrNo40Ci09/ks0tEXo+KZNTrveCX3guN2LnZ+F3jH+oSJY3PM/r2i2
rN60RGiRk7WNa3KFNqjqlFjO8/rPlwtLYr4f9v7P9bX12Z/ihf7T0/Wm/YTQ
gRryzBfJQs+LDRw4f13o+8tl/OaX/Z/r/eu3JGaGz3+mfNu9PURcaCvZYxcD
Zwp9zr5gzEVJ6HU3xPO0dIXu25E35wkIrRFf7lbgJLTLtbcxN1cInfdKpPU0
IXS47epEf47QWR47nrA3Cd269dDA8q1CL7x025kWKvSOIhShHy70lbrXN2ZF
C13f2/9KZv//me/fgyv0/wPrD9Yf
     "]]}, 
   {RGBColor[1, 0, 0], LineBox[CompressedData["
1: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
iha6vrf/lcz+/3O/fw+u0P8PynKjrg==
     "]]}},
  Axes->True,
  AxesOrigin->{0, 0},
  ImageSize->{703., Automatic},
  PlotRange->{{-90, 90}, {-30, 30}},
  PlotRangeClipping->True,
  PlotRangePadding->{Automatic, Automatic}]], "Output",
 CellChangeTimes->{
  3.4788709849011707`*^9, {3.4788710863719063`*^9, 3.4788711060411377`*^9}, 
   3.4788712799735374`*^9, 3.478871319593972*^9, 3.478871508947587*^9, 
   3.478871694708624*^9, 3.4788717429377584`*^9, 3.478942986855018*^9}]
}, Open  ]]
}, Closed]],

Cell[CellGroupData[{

Cell[TextData[StyleBox["MDHW",
 FontFamily->"Courier"]], "Title",
 CellChangeTimes->{3.4204398284623485`*^9, 3.4788693225667324`*^9},
 Background->RGBColor[1, 1, 0]],

Cell[BoxData[
 RowBox[{"Clear", "[", 
  RowBox[{"APER1", ",", "APER2", ",", "APER3", ",", "APER4", ",", "TILT"}], 
  "]"}]], "Input",
 CellChangeTimes->{3.4204398284623485`*^9, 3.4788693225667324`*^9}],

Cell[BoxData[
 RowBox[{
  RowBox[{"APER1", "=", "70"}], ";", 
  RowBox[{"APER2", "=", "24.5"}], ";", 
  RowBox[{"APER3", "=", "70"}], ";", 
  RowBox[{"APER4", "=", "57"}], ";", 
  RowBox[{"TILT", "=", "0"}], ";"}]], "Input",
 CellChangeTimes->{
  3.4204398284623485`*^9, {3.420439961747864*^9, 3.4204399678261833`*^9}, {
   3.420440017827783*^9, 3.420440020812254*^9}, 3.4788693225823565`*^9}],

Cell[CellGroupData[{

Cell[BoxData[
 RowBox[{"Show", "[", "\[IndentingNewLine]", 
  RowBox[{
   RowBox[{"ParametricPlot", "[", 
    RowBox[{
     RowBox[{"{", 
      RowBox[{
       RowBox[{"MDHW", "[", 
        RowBox[{"x", ",", "0"}], "]"}], ",", 
       RowBox[{"-", 
        RowBox[{"MDHW", "[", 
         RowBox[{"x", ",", "0"}], "]"}]}]}], "}"}], ",", 
     RowBox[{"{", 
      RowBox[{"x", ",", 
       RowBox[{"-", "80"}], ",", "80"}], "}"}], ",", 
     RowBox[{"PlotRange", "\[Rule]", 
      RowBox[{"{", 
       RowBox[{
        RowBox[{"{", 
         RowBox[{
          RowBox[{"-", "80"}], ",", "80"}], "}"}], ",", 
        RowBox[{"{", 
         RowBox[{
          RowBox[{"-", "30"}], ",", "30"}], "}"}]}], "}"}]}], ",", 
     RowBox[{"AspectRatio", "\[Rule]", "Automatic"}], ",", 
     RowBox[{"PlotStyle", "\[Rule]", 
      RowBox[{"{", 
       RowBox[{
        RowBox[{"{", 
         RowBox[{"RGBColor", "[", 
          RowBox[{"1", ",", "0", ",", "0"}], "]"}], "}"}], ",", 
        RowBox[{"{", 
         RowBox[{"RGBColor", "[", 
          RowBox[{"1", ",", "0", ",", "0"}], "]"}], "}"}], ",", 
        RowBox[{"{", 
         RowBox[{"RGBColor", "[", 
          RowBox[{"0", ",", "0", ",", "1"}], "]"}], "}"}], ",", 
        RowBox[{"{", 
         RowBox[{"RGBColor", "[", 
          RowBox[{"0", ",", "0", ",", "1"}], "]"}], "}"}]}], "}"}]}]}], "]"}],
    ",", "\[IndentingNewLine]", 
   RowBox[{"ParametricPlot", "[", 
    RowBox[{
     RowBox[{"{", 
      RowBox[{
       RowBox[{"Rectellipse", "[", 
        RowBox[{
        "x", ",", "APER1", ",", "APER2", ",", "APER3", ",", "APER4", ",", 
         "TILT"}], "]"}], ",", 
       RowBox[{"-", 
        RowBox[{"Rectellipse", "[", 
         RowBox[{
         "x", ",", "APER1", ",", "APER2", ",", "APER3", ",", "APER4", ",", 
          "TILT"}], "]"}]}]}], "}"}], ",", 
     RowBox[{"{", 
      RowBox[{"x", ",", 
       RowBox[{"-", "80"}], ",", "80"}], "}"}], ",", 
     RowBox[{"PlotRange", "\[Rule]", 
      RowBox[{"{", 
       RowBox[{
        RowBox[{"{", 
         RowBox[{
          RowBox[{"-", "80"}], ",", "80"}], "}"}], ",", 
        RowBox[{"{", 
         RowBox[{
          RowBox[{"-", "30"}], ",", "30"}], "}"}]}], "}"}]}], ",", 
     RowBox[{"PlotPoints", "\[Rule]", "60"}], ",", 
     RowBox[{"PlotStyle", "\[Rule]", 
      RowBox[{"{", 
       RowBox[{
        RowBox[{"{", 
         RowBox[{"RGBColor", "[", 
          RowBox[{"0", ",", "0", ",", "1"}], "]"}], "}"}], ",", 
        RowBox[{"{", 
         RowBox[{"RGBColor", "[", 
          RowBox[{"0", ",", "0", ",", "1"}], "]"}], "}"}]}], "}"}]}], ",", 
     RowBox[{"AspectRatio", "\[Rule]", "Automatic"}]}], "]"}]}], 
  "\[IndentingNewLine]", "]"}]], "Input",
 CellChangeTimes->{{3.4203819344616203`*^9, 3.420381955740691*^9}, 
   3.4203821089911737`*^9, 3.4204397902111244`*^9, 3.4204398284623485`*^9, 
   3.420439872760641*^9, 3.420439907480502*^9, {3.42044005631339*^9, 
   3.4204400695013113`*^9}, {3.4731602638346443`*^9, 3.473160265475185*^9}, {
   3.4731603920624533`*^9, 3.4731604077179017`*^9}, 3.4788693225823565`*^9}],

Cell[BoxData[
 GraphicsBox[{{{}, {}, 
    {RGBColor[1, 0, 0], LineBox[CompressedData["
1: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
      "]]}, 
    {RGBColor[1, 0, 0], LineBox[CompressedData["
1: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
      "]]}}, {{}, {}, 
    {RGBColor[0, 0, 1], LineBox[CompressedData["
1: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
Cjm2YS6s+4n8O9ZR/h/j3pXn
      "]]}, 
    {RGBColor[0, 0, 1], LineBox[CompressedData["
1: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
5NiGudi6n8i/Yx3l/wF9b/Jn
      "]]}}},
  Axes->True,
  AxesOrigin->{0, 0},
  PlotRange->{{-80, 80}, {-30, 30}},
  PlotRangeClipping->True,
  PlotRangePadding->{Automatic, Automatic}]], "Output",
 CellChangeTimes->{3.4788695652746086`*^9, 3.4788709859166594`*^9}]
}, Open  ]],

Cell[BoxData[{
 RowBox[{
  RowBox[{"Clear", "[", 
   RowBox[{"x1", ",", "x2", ",", "a", ",", "b", ",", "EX"}], "]"}], 
  ";"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{
   RowBox[{"C1", "   ", "=", " ", 
    RowBox[{"{", 
     RowBox[{"0", ",", " ", "0"}], " ", "}"}]}], ";"}], 
  "                                         ", 
  StyleBox[
   RowBox[{"(*", "  ", 
    RowBox[{"[", "mm", "]"}], "   ", "*)"}],
   FontColor->RGBColor[0, 0, 1]]}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{
   RowBox[{"C2", "   ", "=", " ", 
    RowBox[{"{", 
     RowBox[{"0", ",", " ", 
      RowBox[{
       RowBox[{
        RowBox[{"(", "42.2", ")"}], "/", "2"}], "-", "700"}]}], "}"}]}], 
   ";"}], "      ", 
  StyleBox[
   RowBox[{"(*", "  ", 
    RowBox[{"[", "mm", "]"}], "   ", "*)"}],
   FontColor->RGBColor[0, 0, 1]]}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{
   RowBox[{"C3", "   ", "=", " ", 
    RowBox[{"{", 
     RowBox[{"a", ",", " ", "b"}], "}"}]}], ";"}], "    ", 
  RowBox[{"(*", 
   StyleBox[
    RowBox[{"  ", 
     StyleBox["  ",
      FontColor->RGBColor[0, 0, 1]]}]], 
   StyleBox[
    RowBox[{"[", "mm", "]"}],
    FontColor->RGBColor[0, 0, 1]], 
   StyleBox["   ",
    FontColor->RGBColor[0, 0, 1]], 
   StyleBox["*)",
    FontColor->RGBColor[0, 0, 1]]}], 
  StyleBox["\[IndentingNewLine]",
   FontColor->RGBColor[0, 0, 1]], 
  StyleBox["\[IndentingNewLine]",
   FontColor->RGBColor[0, 0, 1]], 
  StyleBox["\[IndentingNewLine]",
   FontColor->RGBColor[0, 0, 1]]}], "\[IndentingNewLine]", 
 StyleBox[
  RowBox[{
   RowBox[{"R1", "=", "74.7"}], ";"}],
  FontColor->RGBColor[0, 0, 1]], "\[IndentingNewLine]", 
 StyleBox[
  RowBox[{
   RowBox[{"R2", "=", "700"}], ";"}],
  FontColor->RGBColor[0, 0, 1]], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{
   RowBox[{"R3", "=", "10"}], ";"}], 
  "\[IndentingNewLine]"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{
   RowBox[{"y1", "[", "x_", "]"}], "=", 
   RowBox[{
    SqrtBox[
     RowBox[{
      RowBox[{"R1", "^", "2"}], "-", 
      RowBox[{
       RowBox[{"(", 
        RowBox[{"x", "-", 
         RowBox[{"C1", "[", 
          RowBox[{"[", "1", "]"}], "]"}]}], ")"}], "^", "2"}]}]], "+", 
    RowBox[{"C1", "[", 
     RowBox[{"[", "2", "]"}], "]"}]}]}], ";"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{
   RowBox[{"y2", "[", "x_", "]"}], "=", 
   RowBox[{
    SqrtBox[
     RowBox[{
      RowBox[{"R2", "^", "2"}], "-", 
      RowBox[{
       RowBox[{"(", 
        RowBox[{"x", "-", 
         RowBox[{"C2", "[", 
          RowBox[{"[", "1", "]"}], "]"}]}], ")"}], "^", "2"}]}]], "+", 
    RowBox[{"C2", "[", 
     RowBox[{"[", "2", "]"}], "]"}]}]}], ";"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{
   RowBox[{"y3", "[", "x_", "]"}], "=", 
   RowBox[{
    SqrtBox[
     RowBox[{
      RowBox[{"R3", "^", "2"}], "-", 
      RowBox[{
       RowBox[{"(", 
        RowBox[{"x", "-", 
         RowBox[{"C3", "[", 
          RowBox[{"[", "1", "]"}], "]"}]}], ")"}], "^", "2"}]}]], "+", 
    RowBox[{"C3", "[", 
     RowBox[{"[", "2", "]"}], "]"}]}]}], ";"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{
   RowBox[{"y4", "[", "x_", "]"}], "=", 
   RowBox[{
    RowBox[{"y1", "'"}], "[", "x", "]"}]}], ";"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{
   RowBox[{"y5", "[", "x_", "]"}], "=", 
   RowBox[{
    RowBox[{"y2", "'"}], "[", "x", "]"}]}], ";"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{
   RowBox[{
    RowBox[{"y6", "[", "x_", "]"}], "=", 
    RowBox[{
     RowBox[{"y3", "'"}], "[", "x", "]"}]}], ";"}], 
  "\[IndentingNewLine]"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{"Off", "[", 
   RowBox[{"FindMinimum", "::", "\"\<lstol\>\""}], "]"}], ";", 
  RowBox[{"EX", "=", 
   RowBox[{"FindMinimum", "[", 
    RowBox[{
     RowBox[{
      RowBox[{
       RowBox[{"(", 
        RowBox[{
         RowBox[{"y2", "[", "x1", "]"}], "-", 
         RowBox[{"y3", "[", "x1", "]"}]}], ")"}], "*", 
       RowBox[{"Conjugate", "[", 
        RowBox[{"(", 
         RowBox[{
          RowBox[{"y2", "[", "x1", "]"}], "-", 
          RowBox[{"y3", "[", "x1", "]"}]}], ")"}], "]"}]}], "+", 
      RowBox[{
       RowBox[{"(", 
        RowBox[{
         RowBox[{"y1", "[", "x2", "]"}], "-", 
         RowBox[{"y3", "[", "x2", "]"}]}], ")"}], "*", 
       RowBox[{"Conjugate", "[", 
        RowBox[{"(", 
         RowBox[{
          RowBox[{"y1", "[", "x2", "]"}], "-", 
          RowBox[{"y3", "[", "x2", "]"}]}], ")"}], "]"}]}], "+", 
      RowBox[{
       RowBox[{"(", 
        RowBox[{
         RowBox[{"y5", "[", "x1", "]"}], "-", 
         RowBox[{"y6", "[", "x1", "]"}]}], ")"}], "*", 
       RowBox[{"Conjugate", "[", 
        RowBox[{"(", 
         RowBox[{
          RowBox[{"y5", "[", "x1", "]"}], "-", 
          RowBox[{"y6", "[", "x1", "]"}]}], ")"}], "]"}]}], "+", 
      RowBox[{
       RowBox[{"(", 
        RowBox[{
         RowBox[{"y4", "[", "x2", "]"}], "-", 
         RowBox[{"y6", "[", "x2", "]"}]}], ")"}], "*", 
       RowBox[{"Conjugate", "[", 
        RowBox[{"(", 
         RowBox[{
          RowBox[{"y4", "[", "x2", "]"}], "-", 
          RowBox[{"y6", "[", "x2", "]"}]}], ")"}], "]"}]}]}], ",", 
     RowBox[{"{", 
      RowBox[{
       RowBox[{"{", 
        RowBox[{"x1", ",", "75"}], "}"}], ",", 
       RowBox[{"{", 
        RowBox[{"x2", ",", "64"}], "}"}], ",", 
       RowBox[{"{", 
        RowBox[{"a", ",", "64.2"}], "}"}], ",", 
       RowBox[{"{", 
        RowBox[{"b", ",", "8.2"}], "}"}]}], "}"}], ",", 
     RowBox[{"MaxIterations", "\[Rule]", "50"}]}], "]"}]}], 
  ";"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{
   RowBox[{"On", "[", 
    RowBox[{"FindMinimum", "::", "\"\<lstol\>\""}], "]"}], ";"}], 
  "\[IndentingNewLine]", 
  "\[IndentingNewLine]"}], "\[IndentingNewLine]"}], "Input",
 CellChangeTimes->{{3.4789504319535027`*^9, 3.4789504474208665`*^9}, {
   3.4789510893789673`*^9, 3.4789513190302634`*^9}, {3.4789513679321313`*^9, 
   3.478951383102647*^9}, 3.478951506966548*^9, {3.4789519457084827`*^9, 
   3.4789520122806425`*^9}}],

Cell[CellGroupData[{

Cell[BoxData["EX"], "Input",
 CellChangeTimes->{{3.4789513272482767`*^9, 3.4789513274826307`*^9}}],

Cell[BoxData[
 RowBox[{"{", 
  RowBox[{"1.5775214059964072`*^-7", ",", 
   RowBox[{"{", 
    RowBox[{
     RowBox[{"65.12009864096866`", "\[Rule]", "65.12009864096866`"}], ",", 
     RowBox[{"74.11107851120781`", "\[Rule]", "74.11107851120781`"}], ",", 
     RowBox[{"64.18991622763764`", "\[Rule]", "64.18991622763764`"}], ",", 
     RowBox[{"8.107986893306824`", "\[Rule]", "8.107986893306824`"}]}], 
    "}"}]}], "}"}]], "Output",
 CellChangeTimes->{
  3.4789513285294123`*^9, {3.4789514026008997`*^9, 3.4789514085066204`*^9}, 
   3.4789515117004986`*^9, 3.4789519925792828`*^9, 3.4789529264174786`*^9}]
}, Open  ]],

Cell[CellGroupData[{

Cell[BoxData["C2"], "Input",
 CellChangeTimes->{{3.478951437394657*^9, 3.4789514437065916`*^9}, {
  3.478951476391163*^9, 3.478951476844247*^9}, {3.4789531825664005`*^9, 
  3.478953187784683*^9}}],

Cell[BoxData[
 RowBox[{"{", 
  RowBox[{"0", ",", 
   RowBox[{"-", "678.9`"}]}], "}"}]], "Output",
 CellChangeTimes->{{3.4789514389726405`*^9, 3.4789514443315353`*^9}, 
   3.478951477281708*^9, {3.4789531849255643`*^9, 3.4789531883002615`*^9}}]
}, Open  ]],

Cell[BoxData[
 RowBox[{
  RowBox[{"a", "=", "64.18991622763764"}], ";"}]], "Input",
 CellChangeTimes->{{3.4789518330779505`*^9, 3.4789518427333355`*^9}, 
   3.4789535696410904`*^9}],

Cell[BoxData[
 RowBox[{
  RowBox[{"b", "=", "8.107986893306824"}], ";"}]], "Input",
 CellChangeTimes->{{3.4789518449518867`*^9, 3.4789518535917377`*^9}, 
   3.4789535665944886`*^9}],

Cell[BoxData[
 RowBox[{
  RowBox[{"x1", "=", "65.12009864096866"}], ";"}]], "Input",
 CellChangeTimes->{{3.4788715496150365`*^9, 3.478871551739805*^9}, {
   3.478951796471856*^9, 3.4789517978936033`*^9}, 3.47895356200115*^9}],

Cell[BoxData[
 RowBox[{
  RowBox[{"x2", "=", "74.11107851120781"}], ";"}]], "Input",
 CellChangeTimes->{{3.478871554208287*^9, 3.478871554551999*^9}, {
   3.478951806970915*^9, 3.478951808345792*^9}, 3.4789535586264524`*^9}],

Cell[CellGroupData[{

Cell[BoxData[
 RowBox[{"y3", "[", "x1", "]"}]], "Input",
 CellChangeTimes->{{3.4789518229382343`*^9, 3.4789518266722746`*^9}}],

Cell[BoxData["18.06463094027012`"], "Output",
 CellChangeTimes->{{3.478951827219101*^9, 3.4789518567945757`*^9}}]
}, Open  ]],

Cell[BoxData["18.06463094027012"], "Input",
 CellChangeTimes->{3.478953133039589*^9}],

Cell[CellGroupData[{

Cell[BoxData[
 RowBox[{"y3", "[", "x2", "]"}]], "Input",
 CellChangeTimes->{{3.47895187426176*^9, 3.478951877823941*^9}}],

Cell[BoxData["9.361198345163512`"], "Output",
 CellChangeTimes->{3.4789518783863907`*^9}]
}, Open  ]],

Cell[BoxData["9.361198345163512"], "Input",
 CellChangeTimes->{3.4789531410076246`*^9}]
}, Closed]],

Cell[CellGroupData[{

Cell[TextData[StyleBox["TPST ",
 FontFamily->"Courier"]], "Title",
 CellChangeTimes->{{3.5140155335079975`*^9, 3.5140155491017475`*^9}, {
  3.63637330054379*^9, 3.636373302431426*^9}, {3.6363743964528675`*^9, 
  3.636374399557327*^9}},
 Background->RGBColor[1, 1, 0]],

Cell[CellGroupData[{

Cell[BoxData[{
 RowBox[{
  RowBox[{"Hor", "=", 
   RowBox[{"40", "+", 
    RowBox[{"273", "/", "2."}]}]}], ";"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{"HorExt", " ", "=", " ", 
   RowBox[{"Hor", "/", "2."}]}], ";"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{"HorInt", " ", "=", " ", 
   RowBox[{"Hor", "/", "2."}]}], ";"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{"Ver", "=", 
   RowBox[{"273", "/", "2."}]}], ";"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{"TILT", "=", "0.0"}], ";"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{
   RowBox[{"offset", "=", 
    RowBox[{"40.", "-", "HorExt"}]}], ";"}], 
  "\[IndentingNewLine]"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{
   RowBox[{"XY", "=", 
    RowBox[{"{", 
     RowBox[{
      RowBox[{"{", 
       RowBox[{"40", ",", "0"}], "}"}], ",", 
      RowBox[{"{", 
       RowBox[{"40", ",", 
        RowBox[{"273", "/", "2"}]}], "}"}], ",", 
      RowBox[{"{", 
       RowBox[{
        RowBox[{
         RowBox[{"-", "273"}], "/", "2"}], ",", 
        RowBox[{"273", "/", "2"}]}], "}"}], ",", 
      RowBox[{"{", 
       RowBox[{
        RowBox[{
         RowBox[{"-", "273"}], "/", "2"}], ",", 
        RowBox[{
         RowBox[{"-", "273"}], "/", "2"}]}], "}"}], ",", 
      RowBox[{"{", 
       RowBox[{"40", ",", 
        RowBox[{
         RowBox[{"-", "273"}], "/", "2"}]}], "}"}], ",", 
      RowBox[{"{", 
       RowBox[{"40", ",", "0"}], "}"}]}], "}"}]}], ";"}], 
  "\[IndentingNewLine]"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{
   RowBox[{"neg", "[", "y_", "]"}], ":=", 
   RowBox[{"{", 
    RowBox[{
     RowBox[{"y", "[", 
      RowBox[{"[", "1", "]"}], "]"}], ",", 
     RowBox[{"-", 
      RowBox[{"y", "[", 
       RowBox[{"[", "2", "]"}], "]"}]}]}], "}"}]}], 
  ";"}], "\[IndentingNewLine]", 
 RowBox[{"Show", "[", "\[IndentingNewLine]", 
  RowBox[{
   RowBox[{"ListPlot", "[", 
    RowBox[{"XY", ",", 
     RowBox[{"Joined", "\[Rule]", "True"}], ",", 
     RowBox[{"PlotRange", "\[Rule]", 
      RowBox[{"{", 
       RowBox[{
        RowBox[{"{", 
         RowBox[{"200", ",", 
          RowBox[{"-", "200"}]}], "}"}], ",", 
        RowBox[{"{", 
         RowBox[{
          RowBox[{"-", "200"}], ",", "200"}], "}"}]}], "}"}]}], ",", 
     RowBox[{"PlotStyle", "\[Rule]", 
      RowBox[{"{", 
       RowBox[{
        RowBox[{"Thickness", "[", "0.02", "]"}], ",", "Blue"}], "}"}]}], ",", 
     
     RowBox[{"AspectRatio", "\[Rule]", "1."}]}], "]"}], ",", 
   "\[IndentingNewLine]", "\[IndentingNewLine]", 
   RowBox[{"ParametricPlot", "[", 
    RowBox[{
     RowBox[{"{", 
      RowBox[{
       RowBox[{"RECTANGLE", "[", 
        RowBox[{
        "x", ",", "HorExt", ",", "HorInt", ",", "Ver", ",", "offset", ",", 
         "TILT"}], "]"}], ",", 
       RowBox[{"neg", "[", 
        RowBox[{"RECTANGLE", "[", 
         RowBox[{
         "x", ",", "HorExt", ",", "HorInt", ",", "Ver", ",", "offset", ",", 
          "TILT"}], "]"}], "]"}]}], "}"}], ",", 
     RowBox[{"{", 
      RowBox[{"x", ",", 
       RowBox[{"-", "140"}], ",", "41"}], "}"}], ",", 
     RowBox[{"PlotPoints", "\[Rule]", "800"}], ",", 
     RowBox[{"PlotStyle", "\[Rule]", 
      RowBox[{"{", 
       RowBox[{"Red", ",", "Red"}], "}"}]}]}], "]"}]}], "\[IndentingNewLine]",
   "]"}]}], "Input",
 CellChangeTimes->{{3.636373488390605*^9, 3.636373538373966*^9}, {
  3.636373781473441*^9, 3.6363738039690733`*^9}, {3.636373941345315*^9, 
  3.6363739429209456`*^9}, {3.6363744595092797`*^9, 3.6363744619897275`*^9}, {
  3.636374520615655*^9, 3.6363745482749867`*^9}, {3.636374586511322*^9, 
  3.636374598913561*^9}, {3.6363747761953697`*^9, 3.6363747904384437`*^9}, {
  3.6363752479984555`*^9, 3.6363752484820647`*^9}, {3.636375560549494*^9, 
  3.636375560721097*^9}, {3.6363758022293415`*^9, 3.636375838593641*^9}, {
  3.636375927094143*^9, 3.636375929090981*^9}, {3.6363762286479416`*^9, 
  3.6363762287883444`*^9}, {3.6363766589978175`*^9, 3.636376711040418*^9}, {
  3.636376768121916*^9, 3.636376795141636*^9}, {3.636376901395279*^9, 
  3.6363769125962944`*^9}, {3.6363772025618725`*^9, 3.6363772955396605`*^9}}],

Cell[BoxData[
 GraphicsBox[{{{}, {{}, {}, 
     {RGBColor[0, 0, 1], Thickness[0.02], 
      LineBox[{{40., 0.}, {40., 136.5}, {-136.5, 136.5}, {-136.5, -136.5}, {
       40., -136.5}, {40., 0.}}]}}, {}}, {{}, {}, 
    {RGBColor[1, 0, 0], LineBox[CompressedData["
1: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
7f5fJw==
      "]]}, 
    {RGBColor[1, 0, 0], LineBox[CompressedData["
1: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
DruUyl/5xAVnCXY/+EYDn73n4Nn4x5xwyno5ZfAnOOJo5JHqSljcobhg/RZc
vDfKczwMXmip5Px0BJYwuKl2whAWfDkqGCMBv++6+auADvbsnVYLmNxPuO7s
fS+d93Afb5tbSin8o/R+Z3IynDPQJZcSDO+nKF7TPgw3yFMk+WvDMxNP2AtE
YcosWoYrlHDnj5pp9zEzwl4qYze7WuGpoJqSsUew1IHp6tVE2FTordZzf1gm
nCzvrC3cMfroc4MW7GJEHVYmCBeoVTHnk8O9wrzchsP7CH/ZPDPs1QRfTxLK
TH4IyzEtt7hfgy/zKI+oe8O5cv2v0qzgYjVV3rs74ICP43b5vLDoCWPWQyum
hFM3CcYl98FvtpnNdzXA322lO58/gEuZnW/djYZP1+h9U/CA//ilDew1hbdV
m74/rgjbLT/cIccKa7a6Rc/N7yU8kp10e9dXOOjM6a261XBTd/Z9zSx4RSkq
sS8CXr7Rt4vZDS6NShjW3QNb+87845GBn07nLf1mhD/7db+wnzMh/GPm6bJH
F1y0OiYaUgk7kL+tU06HPzOLiAWeg+kfd3rXOsOSu5S2F+rDq17jw+kScPVV
M3olGtiwROqv1bgx4Ugvx9agNriYX4dn9xM42THkAFsSbJgvZ3YqEO4Zj6n3
toNlaw2E/bXho9G584LC8HH7iOs25LB4XTl7wsgewm/5Ulh838DStJ0LloWw
xfql+y/jYdfJ741ffWF5z/TOOWt4cGDV5qkabD5W/dqXH45anF2u2zAinLve
kVM+CEekMu4saoINpP4Y782D2+vM+c7GwOwTNN33T8H6DF70geawzAsZmX0q
cE+wE+MTbjhATsf9+dJuws0+wYWNfTBVkfPxwDqYYbZ6rPIe3Nrkb7UUCQfc
+Lxj6Dj8efYm5TtTWNRofY+jPKya3XcglAXedJNnd+afXYSrQ9afuH2C5f7o
Uss9h90DFkUu3oZjpuxKzp8nmV/gVgx3I8lfjBAT301Sn8ylx1YK3pSZERbL
AKsqRKSemDbE+i0bMnd/gD+HB7kXl8MB93tyX6bCrbZpnZ/OwQybyM8kOMJU
Bk0U+/Th5isbB5MlSOq9/iEYRQP3JEt0Bk4a4H4dWNc2t8H6sv5Tak9g9lil
N85JcPtwGo/iGdigzcF64xAcUZdi46gN5+Wfa3cVhqO31Ch7UMIHkvMYuEf0
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
E+m2
      "]]}}},
  AspectRatio->1.,
  Axes->True,
  AxesLabel->{None, None},
  AxesOrigin->{0, 0},
  Method->{},
  PlotRange->{{200, -200}, {-200, 200}},
  PlotRangeClipping->True,
  PlotRangePadding->{Automatic, Automatic}]], "Output",
 CellChangeTimes->{
  3.6363732561765366`*^9, 3.6363733100479755`*^9, 3.636373369188712*^9, 
   3.636373545799709*^9, 3.6363736735505657`*^9, 3.6363738118160243`*^9, {
   3.636373885231036*^9, 3.6363739093022995`*^9}, 3.636373950331088*^9, 
   3.6363740196276207`*^9, 3.6363740510154247`*^9, 3.6363744658430014`*^9, {
   3.6363745150307474`*^9, 3.63637452453133*^9}, {3.6363745946078777`*^9, 
   3.636374601690414*^9}, {3.6363746355898657`*^9, 3.6363746505037527`*^9}, {
   3.6363746805343304`*^9, 3.6363746897697077`*^9}, 3.6363747974117775`*^9, {
   3.636374848892768*^9, 3.636374910306351*^9}, 3.6363749499311132`*^9, {
   3.636375019867258*^9, 3.6363750269965954`*^9}, 3.6363752514617224`*^9, 
   3.6363755644963694`*^9, {3.6363758156924005`*^9, 3.6363758449897633`*^9}, {
   3.636375875644353*^9, 3.6363758810732574`*^9}, {3.636375919356394*^9, 
   3.636375932367044*^9}, 3.6363760837055545`*^9, {3.636376116341382*^9, 
   3.6363761312084675`*^9}, {3.6363761973381395`*^9, 3.636376300643326*^9}, 
   3.6363763327487435`*^9, {3.6363763748071527`*^9, 3.6363763821860943`*^9}, 
   3.636376447598152*^9, {3.6363767300727844`*^9, 3.6363768261706324`*^9}, 
   3.6363769174635878`*^9, {3.636377240298999*^9, 3.636377299174531*^9}}]
}, Open  ]]
}, Open  ]]
},
WindowSize->{979, 756},
WindowMargins->{{153, Automatic}, {Automatic, 92}},
PrintingCopies->1,
PrintingPageRange->{Automatic, Automatic},
ShowSelection->True,
FrontEndVersion->"9.0 for Microsoft Windows (32-bit) (January 25, 2013)",
StyleDefinitions->Notebook[{
   Cell[
    CellGroupData[{
      Cell["Style Definitions", "Title"], 
      Cell[
      "Modify the definitions below to change the default appearance of all \
cells in a given style.  Make modifications to any definition using commands \
in the Format menu.", "Text"], 
      Cell[
       CellGroupData[{
         Cell["Style Environment Names", "Section"], 
         Cell[
          StyleData[All, "Working"], PageWidth -> WindowWidth, 
          CellBracketOptions -> {
           "Color" -> RGBColor[0.269993, 0.308507, 0.6]}, 
          CellLabelMargins -> {{12, Inherited}, {Inherited, Inherited}}, 
          ScriptMinSize -> 9], 
         Cell[
          StyleData[All, "Presentation"], PageWidth -> WindowWidth, 
          CellLabelMargins -> {{24, Inherited}, {Inherited, Inherited}}, 
          ScriptMinSize -> 12], 
         Cell[
          StyleData[All, "Condensed"], PageWidth -> WindowWidth, 
          CellLabelMargins -> {{8, Inherited}, {Inherited, Inherited}}, 
          ScriptMinSize -> 8], 
         Cell[
          StyleData[All, "Printout"], PageWidth -> PaperWidth, 
          CellLabelMargins -> {{2, Inherited}, {Inherited, Inherited}}, 
          ScriptMinSize -> 5, 
          PrivateFontOptions -> {"FontType" -> "Outline"}]}, Closed]], 
      Cell[
       CellGroupData[{
         Cell["Notebook Options", "Section"], 
         Cell[
         "The options defined for the style below will be used at the \
Notebook level.", "Text"], 
         Cell[
          StyleData["Notebook"], PageHeaders -> {{
             Cell[
              TextData[{
                CounterBox["Page"]}], "PageNumber"], None, 
             Cell[
              TextData[{
                ValueBox["FileName"]}], "Header"]}, {
             Cell[
              TextData[{
                ValueBox["FileName"]}], "Header"], None, 
             Cell[
              TextData[{
                CounterBox["Page"]}], "PageNumber"]}}, CellFrameLabelMargins -> 
          6, StyleMenuListing -> None]}, Closed]], 
      Cell[
       CellGroupData[{
         Cell["Styles for Headings", "Section"], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["Title"], CellMargins -> {{27, Inherited}, {10, 30}}, 
             CellGroupingRules -> {"TitleGrouping", 0}, PageBreakBelow -> 
             False, DefaultNewInlineCellStyle -> "None", 
             InputAutoReplacements -> {"TeX" -> StyleBox[
                 RowBox[{"T", 
                   AdjustmentBox[
                   "E", BoxMargins -> {{-0.075, -0.085}, {0, 0}}, 
                    BoxBaselineShift -> 0.5], "X"}]], "LaTeX" -> StyleBox[
                 RowBox[{"L", 
                   StyleBox[
                    AdjustmentBox[
                    "A", BoxMargins -> {{-0.36, -0.1}, {0, 0}}, 
                    BoxBaselineShift -> -0.2], FontSize -> Smaller], "T", 
                   AdjustmentBox[
                   "E", BoxMargins -> {{-0.075, -0.085}, {0, 0}}, 
                    BoxBaselineShift -> 0.5], "X"}]], "mma" -> "Mathematica", 
               "Mma" -> "Mathematica", "MMA" -> "Mathematica", 
               "gridMathematica" -> FormBox[
                 RowBox[{"grid", 
                   AdjustmentBox[
                    StyleBox["Mathematica", FontSlant -> "Italic"], 
                    BoxMargins -> {{-0.175, 0}, {0, 0}}]}], TextForm], 
               "webMathematica" -> FormBox[
                 RowBox[{"web", 
                   AdjustmentBox[
                    StyleBox["Mathematica", FontSlant -> "Italic"], 
                    BoxMargins -> {{-0.175, 0}, {0, 0}}]}], TextForm], 
               Inherited}, LineSpacing -> {1, 11}, LanguageCategory -> 
             "NaturalLanguage", CounterIncrements -> "Title", 
             CounterAssignments -> {{"Section", 0}, {"Equation", 0}, {
               "Figure", 0}, {"Subtitle", 0}, {"Subsubtitle", 0}}, FontFamily -> 
             "Helvetica", FontSize -> 36, FontWeight -> "Bold"], 
            Cell[
             StyleData["Title", "Presentation"], 
             CellMargins -> {{27, 10}, {10, 30}}, LineSpacing -> {1, 0}, 
             FontFamily -> "Courier", FontSize -> 44], 
            Cell[
             StyleData["Title", "Condensed"], 
             CellMargins -> {{8, 10}, {4, 8}}, FontSize -> 20], 
            Cell[
             StyleData["Title", "Printout"], 
             CellMargins -> {{2, 10}, {12, 30}}, FontSize -> 24]}, Open]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["Subtitle"], CellMargins -> {{27, Inherited}, {20, 2}},
              CellGroupingRules -> {"TitleGrouping", 10}, PageBreakBelow -> 
             False, DefaultNewInlineCellStyle -> "None", 
             InputAutoReplacements -> {"TeX" -> StyleBox[
                 RowBox[{"T", 
                   AdjustmentBox[
                   "E", BoxMargins -> {{-0.075, -0.085}, {0, 0}}, 
                    BoxBaselineShift -> 0.5], "X"}]], "LaTeX" -> StyleBox[
                 RowBox[{"L", 
                   StyleBox[
                    AdjustmentBox[
                    "A", BoxMargins -> {{-0.36, -0.1}, {0, 0}}, 
                    BoxBaselineShift -> -0.2], FontSize -> Smaller], "T", 
                   AdjustmentBox[
                   "E", BoxMargins -> {{-0.075, -0.085}, {0, 0}}, 
                    BoxBaselineShift -> 0.5], "X"}]], "mma" -> "Mathematica", 
               "Mma" -> "Mathematica", "MMA" -> "Mathematica", 
               "gridMathematica" -> FormBox[
                 RowBox[{"grid", 
                   AdjustmentBox[
                    StyleBox["Mathematica", FontSlant -> "Italic"], 
                    BoxMargins -> {{-0.175, 0}, {0, 0}}]}], TextForm], 
               "webMathematica" -> FormBox[
                 RowBox[{"web", 
                   AdjustmentBox[
                    StyleBox["Mathematica", FontSlant -> "Italic"], 
                    BoxMargins -> {{-0.175, 0}, {0, 0}}]}], TextForm], 
               Inherited}, LanguageCategory -> "NaturalLanguage", 
             CounterIncrements -> "Subtitle", 
             CounterAssignments -> {{"Section", 0}, {"Equation", 0}, {
               "Figure", 0}, {"Subsubtitle", 0}}, FontFamily -> "Helvetica", 
             FontSize -> 24], 
            Cell[
             StyleData["Subtitle", "Presentation"], 
             CellMargins -> {{27, 10}, {20, 2}}, LineSpacing -> {1, 0}, 
             FontSize -> 36], 
            Cell[
             StyleData["Subtitle", "Condensed"], 
             CellMargins -> {{8, 10}, {4, 4}}, FontSize -> 14], 
            Cell[
             StyleData["Subtitle", "Printout"], 
             CellMargins -> {{2, 10}, {12, 8}}, FontSize -> 18]}, Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["Subsubtitle"], 
             CellMargins -> {{27, Inherited}, {8, 2}}, 
             CellGroupingRules -> {"TitleGrouping", 20}, PageBreakBelow -> 
             False, DefaultNewInlineCellStyle -> "None", 
             InputAutoReplacements -> {"TeX" -> StyleBox[
                 RowBox[{"T", 
                   AdjustmentBox[
                   "E", BoxMargins -> {{-0.075, -0.085}, {0, 0}}, 
                    BoxBaselineShift -> 0.5], "X"}]], "LaTeX" -> StyleBox[
                 RowBox[{"L", 
                   StyleBox[
                    AdjustmentBox[
                    "A", BoxMargins -> {{-0.36, -0.1}, {0, 0}}, 
                    BoxBaselineShift -> -0.2], FontSize -> Smaller], "T", 
                   AdjustmentBox[
                   "E", BoxMargins -> {{-0.075, -0.085}, {0, 0}}, 
                    BoxBaselineShift -> 0.5], "X"}]], "mma" -> "Mathematica", 
               "Mma" -> "Mathematica", "MMA" -> "Mathematica", 
               "gridMathematica" -> FormBox[
                 RowBox[{"grid", 
                   AdjustmentBox[
                    StyleBox["Mathematica", FontSlant -> "Italic"], 
                    BoxMargins -> {{-0.175, 0}, {0, 0}}]}], TextForm], 
               "webMathematica" -> FormBox[
                 RowBox[{"web", 
                   AdjustmentBox[
                    StyleBox["Mathematica", FontSlant -> "Italic"], 
                    BoxMargins -> {{-0.175, 0}, {0, 0}}]}], TextForm], 
               Inherited}, LanguageCategory -> "NaturalLanguage", 
             CounterIncrements -> "Subsubtitle", 
             CounterAssignments -> {{"Section", 0}, {"Equation", 0}, {
               "Figure", 0}}, FontFamily -> "Helvetica", FontSize -> 16], 
            Cell[
             StyleData["Subsubtitle", "Presentation"], 
             CellMargins -> {{24, 10}, {20, 20}}, LineSpacing -> {1, 0}, 
             FontSize -> 24], 
            Cell[
             StyleData["Subsubtitle", "Condensed"], 
             CellMargins -> {{8, 10}, {8, 8}}, FontSize -> 12], 
            Cell[
             StyleData["Subsubtitle", "Printout"], 
             CellMargins -> {{2, 10}, {12, 8}}, FontSize -> 14]}, Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["Section"], CellFrame -> {{0, 0}, {0, 1}}, 
             CellMargins -> {{27, Inherited}, {8, 34}}, 
             CellGroupingRules -> {"SectionGrouping", 30}, PageBreakBelow -> 
             False, CellFrameMargins -> 4, DefaultNewInlineCellStyle -> 
             "None", InputAutoReplacements -> {"TeX" -> StyleBox[
                 RowBox[{"T", 
                   AdjustmentBox[
                   "E", BoxMargins -> {{-0.075, -0.085}, {0, 0}}, 
                    BoxBaselineShift -> 0.5], "X"}]], "LaTeX" -> StyleBox[
                 RowBox[{"L", 
                   StyleBox[
                    AdjustmentBox[
                    "A", BoxMargins -> {{-0.36, -0.1}, {0, 0}}, 
                    BoxBaselineShift -> -0.2], FontSize -> Smaller], "T", 
                   AdjustmentBox[
                   "E", BoxMargins -> {{-0.075, -0.085}, {0, 0}}, 
                    BoxBaselineShift -> 0.5], "X"}]], "mma" -> "Mathematica", 
               "Mma" -> "Mathematica", "MMA" -> "Mathematica", 
               "gridMathematica" -> FormBox[
                 RowBox[{"grid", 
                   AdjustmentBox[
                    StyleBox["Mathematica", FontSlant -> "Italic"], 
                    BoxMargins -> {{-0.175, 0}, {0, 0}}]}], TextForm], 
               "webMathematica" -> FormBox[
                 RowBox[{"web", 
                   AdjustmentBox[
                    StyleBox["Mathematica", FontSlant -> "Italic"], 
                    BoxMargins -> {{-0.175, 0}, {0, 0}}]}], TextForm], 
               Inherited}, LineSpacing -> {1, 2}, LanguageCategory -> 
             "NaturalLanguage", CounterIncrements -> "Section", 
             CounterAssignments -> {{"Subsection", 0}, {"Subsubsection", 0}}, 
             FontFamily -> "Helvetica", FontSize -> 20, FontWeight -> "Bold"], 
            Cell[
             StyleData["Section", "Presentation"], 
             CellMargins -> {{40, 10}, {11, 32}}, LineSpacing -> {1, 0}, 
             FontSize -> 24], 
            Cell[
             StyleData["Section", "Condensed"], 
             CellMargins -> {{18, Inherited}, {6, 12}}, FontSize -> 12], 
            Cell[
             StyleData["Section", "Printout"], 
             CellMargins -> {{2, 0}, {7, 22}}, FontSize -> 14]}, Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["Subsection"], CellDingbat -> "\[FilledSmallSquare]", 
             CellMargins -> {{60, Inherited}, {8, 12}}, 
             CellGroupingRules -> {"SectionGrouping", 40}, PageBreakBelow -> 
             False, DefaultNewInlineCellStyle -> "None", 
             InputAutoReplacements -> {"TeX" -> StyleBox[
                 RowBox[{"T", 
                   AdjustmentBox[
                   "E", BoxMargins -> {{-0.075, -0.085}, {0, 0}}, 
                    BoxBaselineShift -> 0.5], "X"}]], "LaTeX" -> StyleBox[
                 RowBox[{"L", 
                   StyleBox[
                    AdjustmentBox[
                    "A", BoxMargins -> {{-0.36, -0.1}, {0, 0}}, 
                    BoxBaselineShift -> -0.2], FontSize -> Smaller], "T", 
                   AdjustmentBox[
                   "E", BoxMargins -> {{-0.075, -0.085}, {0, 0}}, 
                    BoxBaselineShift -> 0.5], "X"}]], "mma" -> "Mathematica", 
               "Mma" -> "Mathematica", "MMA" -> "Mathematica", 
               "gridMathematica" -> FormBox[
                 RowBox[{"grid", 
                   AdjustmentBox[
                    StyleBox["Mathematica", FontSlant -> "Italic"], 
                    BoxMargins -> {{-0.175, 0}, {0, 0}}]}], TextForm], 
               "webMathematica" -> FormBox[
                 RowBox[{"web", 
                   AdjustmentBox[
                    StyleBox["Mathematica", FontSlant -> "Italic"], 
                    BoxMargins -> {{-0.175, 0}, {0, 0}}]}], TextForm], 
               Inherited}, LanguageCategory -> "NaturalLanguage", 
             CounterIncrements -> "Subsection", 
             CounterAssignments -> {{"Subsubsection", 0}}, FontFamily -> 
             "Helvetica", FontSize -> 14, FontWeight -> "Bold"], 
            Cell[
             StyleData["Subsection", "Presentation"], 
             CellMargins -> {{36, 10}, {11, 32}}, LineSpacing -> {1, 0}, 
             FontSize -> 22], 
            Cell[
             StyleData["Subsection", "Condensed"], 
             CellMargins -> {{16, Inherited}, {6, 12}}, FontSize -> 12], 
            Cell[
             StyleData["Subsection", "Printout"], 
             CellMargins -> {{9, 0}, {7, 22}}, FontSize -> 12]}, Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["Subsubsection"], CellDingbat -> 
             "\[FilledSmallSquare]", 
             CellMargins -> {{60, Inherited}, {2, 10}}, 
             CellGroupingRules -> {"SectionGrouping", 50}, PageBreakBelow -> 
             False, DefaultNewInlineCellStyle -> "None", 
             InputAutoReplacements -> {"TeX" -> StyleBox[
                 RowBox[{"T", 
                   AdjustmentBox[
                   "E", BoxMargins -> {{-0.075, -0.085}, {0, 0}}, 
                    BoxBaselineShift -> 0.5], "X"}]], "LaTeX" -> StyleBox[
                 RowBox[{"L", 
                   StyleBox[
                    AdjustmentBox[
                    "A", BoxMargins -> {{-0.36, -0.1}, {0, 0}}, 
                    BoxBaselineShift -> -0.2], FontSize -> Smaller], "T", 
                   AdjustmentBox[
                   "E", BoxMargins -> {{-0.075, -0.085}, {0, 0}}, 
                    BoxBaselineShift -> 0.5], "X"}]], "mma" -> "Mathematica", 
               "Mma" -> "Mathematica", "MMA" -> "Mathematica", 
               "gridMathematica" -> FormBox[
                 RowBox[{"grid", 
                   AdjustmentBox[
                    StyleBox["Mathematica", FontSlant -> "Italic"], 
                    BoxMargins -> {{-0.175, 0}, {0, 0}}]}], TextForm], 
               "webMathematica" -> FormBox[
                 RowBox[{"web", 
                   AdjustmentBox[
                    StyleBox["Mathematica", FontSlant -> "Italic"], 
                    BoxMargins -> {{-0.175, 0}, {0, 0}}]}], TextForm], 
               Inherited}, LanguageCategory -> "NaturalLanguage", 
             CounterIncrements -> "Subsubsection", FontFamily -> "Times", 
             FontWeight -> "Bold"], 
            Cell[
             StyleData["Subsubsection", "Presentation"], 
             CellMargins -> {{34, 10}, {11, 26}}, LineSpacing -> {1, 0}, 
             FontSize -> 18], 
            Cell[
             StyleData["Subsubsection", "Condensed"], 
             CellMargins -> {{17, Inherited}, {6, 12}}, FontSize -> 10], 
            Cell[
             StyleData["Subsubsection", "Printout"], 
             CellMargins -> {{9, 0}, {7, 14}}, FontSize -> 11]}, Closed]]}, 
        Open]], 
      Cell[
       CellGroupData[{
         Cell["Styles for Body Text", "Section"], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["Text"], CellMargins -> {{60, 10}, {7, 7}}, 
             InputAutoReplacements -> {"TeX" -> StyleBox[
                 RowBox[{"T", 
                   AdjustmentBox[
                   "E", BoxMargins -> {{-0.075, -0.085}, {0, 0}}, 
                    BoxBaselineShift -> 0.5], "X"}]], "LaTeX" -> StyleBox[
                 RowBox[{"L", 
                   StyleBox[
                    AdjustmentBox[
                    "A", BoxMargins -> {{-0.36, -0.1}, {0, 0}}, 
                    BoxBaselineShift -> -0.2], FontSize -> Smaller], "T", 
                   AdjustmentBox[
                   "E", BoxMargins -> {{-0.075, -0.085}, {0, 0}}, 
                    BoxBaselineShift -> 0.5], "X"}]], "mma" -> "Mathematica", 
               "Mma" -> "Mathematica", "MMA" -> "Mathematica", 
               "gridMathematica" -> FormBox[
                 RowBox[{"grid", 
                   AdjustmentBox[
                    StyleBox["Mathematica", FontSlant -> "Italic"], 
                    BoxMargins -> {{-0.175, 0}, {0, 0}}]}], TextForm], 
               "webMathematica" -> FormBox[
                 RowBox[{"web", 
                   AdjustmentBox[
                    StyleBox["Mathematica", FontSlant -> "Italic"], 
                    BoxMargins -> {{-0.175, 0}, {0, 0}}]}], TextForm], 
               Inherited}, LineSpacing -> {1, 3}, CounterIncrements -> 
             "Text"], 
            Cell[
             StyleData["Text", "Presentation"], 
             CellMargins -> {{24, 10}, {10, 10}}, LineSpacing -> {1, 5}, 
             FontSize -> 16], 
            Cell[
             StyleData["Text", "Condensed"], CellMargins -> {{8, 10}, {6, 6}},
              LineSpacing -> {1, 1}, FontSize -> 11], 
            Cell[
             StyleData["Text", "Printout"], CellMargins -> {{2, 2}, {6, 6}}, 
             TextJustification -> 0.5, Hyphenation -> True, FontSize -> 10]}, 
           Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["SmallText"], CellMargins -> {{60, 10}, {6, 6}}, 
             DefaultNewInlineCellStyle -> "None", LineSpacing -> {1, 3}, 
             LanguageCategory -> "NaturalLanguage", CounterIncrements -> 
             "SmallText", FontFamily -> "Helvetica", FontSize -> 9], 
            Cell[
             StyleData["SmallText", "Presentation"], 
             CellMargins -> {{24, 10}, {8, 8}}, LineSpacing -> {1, 5}, 
             FontSize -> 12], 
            Cell[
             StyleData["SmallText", "Condensed"], 
             CellMargins -> {{8, 10}, {5, 5}}, LineSpacing -> {1, 2}, 
             FontSize -> 9], 
            Cell[
             StyleData["SmallText", "Printout"], 
             CellMargins -> {{2, 2}, {5, 5}}, TextJustification -> 0.5, 
             Hyphenation -> True, FontSize -> 7]}, Closed]]}, Closed]], 
      Cell[
       CellGroupData[{
         Cell["Styles for Input/Output", "Section"], 
         Cell[
         "The cells in this section define styles used for input and output \
to the kernel.  Be careful when modifying, renaming, or removing these \
styles, because the front end associates special meanings with these style \
names. Some attributes for these styles are actually set in FormatType Styles \
(in the last section of this stylesheet). ", "Text"], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["Input"], CellMargins -> {{66, 10}, {5, 7}}, 
             Evaluatable -> True, CellGroupingRules -> "InputGrouping", 
             CellHorizontalScrolling -> True, PageBreakWithin -> False, 
             GroupPageBreakWithin -> False, DefaultFormatType -> 
             DefaultInputFormatType, "TwoByteSyntaxCharacterAutoReplacement" -> 
             True, HyphenationOptions -> {
              "HyphenationCharacter" -> "\[Continuation]"}, 
             AutoItalicWords -> {}, LanguageCategory -> "Mathematica", 
             FormatType -> InputForm, ShowStringCharacters -> True, 
             NumberMarks -> True, LinebreakAdjustments -> {0.85, 2, 10, 0, 1},
              CounterIncrements -> "Input", FontWeight -> "Bold"], 
            Cell[
             StyleData["Input", "Presentation"], 
             CellMargins -> {{72, Inherited}, {8, 10}}, LineSpacing -> {1, 0},
              FontSize -> 16], 
            Cell[
             StyleData["Input", "Condensed"], 
             CellMargins -> {{40, 10}, {2, 3}}, FontSize -> 11], 
            Cell[
             StyleData["Input", "Printout"], CellMargins -> {{39, 0}, {4, 6}},
              LinebreakAdjustments -> {0.85, 2, 10, 1, 1}, FontSize -> 9]}, 
           Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["InputOnly"], CellMargins -> {{66, 10}, {7, 7}}, 
             Evaluatable -> True, CellGroupingRules -> "InputGrouping", 
             CellHorizontalScrolling -> True, DefaultFormatType -> 
             DefaultInputFormatType, "TwoByteSyntaxCharacterAutoReplacement" -> 
             True, HyphenationOptions -> {
              "HyphenationCharacter" -> "\[Continuation]"}, 
             AutoItalicWords -> {}, LanguageCategory -> "Mathematica", 
             FormatType -> InputForm, ShowStringCharacters -> True, 
             NumberMarks -> True, LinebreakAdjustments -> {0.85, 2, 10, 0, 1},
              CounterIncrements -> "Input", StyleMenuListing -> None, 
             FontWeight -> "Bold"], 
            Cell[
             StyleData["InputOnly", "Presentation"], 
             CellMargins -> {{72, Inherited}, {8, 10}}, LineSpacing -> {1, 0},
              FontSize -> 16], 
            Cell[
             StyleData["InputOnly", "Condensed"], 
             CellMargins -> {{40, 10}, {2, 3}}, FontSize -> 11], 
            Cell[
             StyleData["InputOnly", "Printout"], 
             CellMargins -> {{39, 0}, {4, 6}}, 
             LinebreakAdjustments -> {0.85, 2, 10, 1, 1}, FontSize -> 9]}, 
           Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["Output"], CellMargins -> {{66, 10}, {7, 5}}, 
             CellEditDuplicate -> True, CellGroupingRules -> "OutputGrouping",
              CellHorizontalScrolling -> True, PageBreakWithin -> False, 
             GroupPageBreakWithin -> False, GeneratedCell -> True, 
             CellAutoOverwrite -> True, DefaultFormatType -> 
             DefaultOutputFormatType, "TwoByteSyntaxCharacterAutoReplacement" -> 
             True, HyphenationOptions -> {
              "HyphenationCharacter" -> "\[Continuation]"}, 
             AutoItalicWords -> {}, LanguageCategory -> None, FormatType -> 
             InputForm, CounterIncrements -> "Output"], 
            Cell[
             StyleData["Output", "Presentation"], 
             CellMargins -> {{72, Inherited}, {10, 8}}, LineSpacing -> {1, 0},
              FontSize -> 16], 
            Cell[
             StyleData["Output", "Condensed"], 
             CellMargins -> {{41, Inherited}, {3, 2}}, FontSize -> 11], 
            Cell[
             StyleData["Output", "Printout"], 
             CellMargins -> {{39, 0}, {6, 4}}, FontSize -> 9]}, Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["Message"], 
             CellMargins -> {{66, Inherited}, {Inherited, Inherited}}, 
             CellGroupingRules -> "OutputGrouping", PageBreakWithin -> False, 
             GroupPageBreakWithin -> False, GeneratedCell -> True, 
             CellAutoOverwrite -> True, ShowCellLabel -> False, 
             DefaultFormatType -> DefaultOutputFormatType, 
             "TwoByteSyntaxCharacterAutoReplacement" -> True, 
             HyphenationOptions -> {
              "HyphenationCharacter" -> "\[Continuation]"}, 
             AutoItalicWords -> {}, LanguageCategory -> None, FormatType -> 
             InputForm, CounterIncrements -> "Message", StyleMenuListing -> 
             None, FontFamily -> "Helvetica", FontSize -> 10, FontColor -> 
             RGBColor[0.6, 0.100008, 0.100008]], 
            Cell[
             StyleData["Message", "Presentation"], 
             CellMargins -> {{72, Inherited}, {Inherited, Inherited}}, 
             LineSpacing -> {1, 0}, FontSize -> 16], 
            Cell[
             StyleData["Message", "Condensed"], 
             CellMargins -> {{41, Inherited}, {Inherited, Inherited}}, 
             FontSize -> 11], 
            Cell[
             StyleData["Message", "Printout"], 
             CellMargins -> {{39, Inherited}, {Inherited, Inherited}}, 
             FontSize -> 7, FontColor -> GrayLevel[0]]}, Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["Print"], 
             CellMargins -> {{66, Inherited}, {Inherited, Inherited}}, 
             CellGroupingRules -> "OutputGrouping", CellHorizontalScrolling -> 
             True, PageBreakWithin -> False, GroupPageBreakWithin -> False, 
             GeneratedCell -> True, CellAutoOverwrite -> True, ShowCellLabel -> 
             False, DefaultFormatType -> DefaultOutputFormatType, 
             "TwoByteSyntaxCharacterAutoReplacement" -> True, 
             HyphenationOptions -> {
              "HyphenationCharacter" -> "\[Continuation]"}, 
             AutoItalicWords -> {}, LanguageCategory -> None, FormatType -> 
             InputForm, CounterIncrements -> "Print", StyleMenuListing -> 
             None], 
            Cell[
             StyleData["Print", "Presentation"], 
             CellMargins -> {{72, Inherited}, {Inherited, Inherited}}, 
             LineSpacing -> {1, 0}, FontSize -> 16], 
            Cell[
             StyleData["Print", "Condensed"], 
             CellMargins -> {{41, Inherited}, {Inherited, Inherited}}, 
             FontSize -> 11], 
            Cell[
             StyleData["Print", "Printout"], 
             CellMargins -> {{39, Inherited}, {Inherited, Inherited}}, 
             FontSize -> 8]}, Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["Graphics"], 
             CellMargins -> {{4, Inherited}, {Inherited, Inherited}}, 
             CellGroupingRules -> "GraphicsGrouping", CellHorizontalScrolling -> 
             True, PageBreakWithin -> False, GeneratedCell -> True, 
             CellAutoOverwrite -> True, ShowCellLabel -> False, 
             DefaultFormatType -> DefaultOutputFormatType, LanguageCategory -> 
             None, FormatType -> InputForm, CounterIncrements -> "Graphics", 
             ImageMargins -> {{43, Inherited}, {Inherited, 0}}, 
             StyleMenuListing -> None, FontFamily -> "Courier", FontSize -> 
             10], 
            Cell[
             StyleData["Graphics", "Presentation"], 
             ImageMargins -> {{62, Inherited}, {Inherited, 0}}], 
            Cell[
             StyleData["Graphics", "Condensed"], 
             ImageMargins -> {{38, Inherited}, {Inherited, 0}}, Magnification -> 
             0.6], 
            Cell[
             StyleData["Graphics", "Printout"], 
             ImageMargins -> {{30, Inherited}, {Inherited, 0}}, Magnification -> 
             0.8]}, Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["CellLabel"], LanguageCategory -> None, 
             StyleMenuListing -> None, FontFamily -> "Helvetica", FontSize -> 
             9, FontColor -> RGBColor[0.269993, 0.308507, 0.6]], 
            Cell[
             StyleData["CellLabel", "Presentation"], FontSize -> 12], 
            Cell[
             StyleData["CellLabel", "Condensed"], FontSize -> 9], 
            Cell[
             StyleData["CellLabel", "Printout"], FontFamily -> "Courier", 
             FontSize -> 8, FontSlant -> "Italic", FontColor -> 
             GrayLevel[0]]}, Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["FrameLabel"], LanguageCategory -> None, 
             StyleMenuListing -> None, FontFamily -> "Helvetica", FontSize -> 
             9], 
            Cell[
             StyleData["FrameLabel", "Presentation"], FontSize -> 12], 
            Cell[
             StyleData["FrameLabel", "Condensed"], FontSize -> 9], 
            Cell[
             StyleData["FrameLabel", "Printout"], FontFamily -> "Courier", 
             FontSize -> 8, FontSlant -> "Italic", FontColor -> 
             GrayLevel[0]]}, Closed]]}, Closed]], 
      Cell[
       CellGroupData[{
         Cell["Inline Formatting", "Section"], 
         Cell[
         "These styles are for modifying individual words or letters in a \
cell exclusive of the cell tag.", "Text"], 
         Cell[
          StyleData["RM"], StyleMenuListing -> None, FontWeight -> "Plain", 
          FontSlant -> "Plain"], 
         Cell[
          StyleData["BF"], StyleMenuListing -> None, FontWeight -> "Bold"], 
         Cell[
          StyleData["IT"], StyleMenuListing -> None, FontSlant -> "Italic"], 
         Cell[
          StyleData["TR"], StyleMenuListing -> None, FontFamily -> "Times", 
          FontWeight -> "Plain", FontSlant -> "Plain"], 
         Cell[
          StyleData["TI"], StyleMenuListing -> None, FontFamily -> "Times", 
          FontWeight -> "Plain", FontSlant -> "Italic"], 
         Cell[
          StyleData["TB"], StyleMenuListing -> None, FontFamily -> "Times", 
          FontWeight -> "Bold", FontSlant -> "Plain"], 
         Cell[
          StyleData["TBI"], StyleMenuListing -> None, FontFamily -> "Times", 
          FontWeight -> "Bold", FontSlant -> "Italic"], 
         Cell[
          StyleData["MR"], "TwoByteSyntaxCharacterAutoReplacement" -> True, 
          HyphenationOptions -> {"HyphenationCharacter" -> "\[Continuation]"},
           StyleMenuListing -> None, FontFamily -> "Courier", FontWeight -> 
          "Plain", FontSlant -> "Plain"], 
         Cell[
          StyleData["MO"], "TwoByteSyntaxCharacterAutoReplacement" -> True, 
          HyphenationOptions -> {"HyphenationCharacter" -> "\[Continuation]"},
           StyleMenuListing -> None, FontFamily -> "Courier", FontWeight -> 
          "Plain", FontSlant -> "Italic"], 
         Cell[
          StyleData["MB"], "TwoByteSyntaxCharacterAutoReplacement" -> True, 
          HyphenationOptions -> {"HyphenationCharacter" -> "\[Continuation]"},
           StyleMenuListing -> None, FontFamily -> "Courier", FontWeight -> 
          "Bold", FontSlant -> "Plain"], 
         Cell[
          StyleData["MBO"], "TwoByteSyntaxCharacterAutoReplacement" -> True, 
          HyphenationOptions -> {"HyphenationCharacter" -> "\[Continuation]"},
           StyleMenuListing -> None, FontFamily -> "Courier", FontWeight -> 
          "Bold", FontSlant -> "Italic"], 
         Cell[
          StyleData["SR"], StyleMenuListing -> None, FontFamily -> 
          "Helvetica", FontWeight -> "Plain", FontSlant -> "Plain"], 
         Cell[
          StyleData["SO"], StyleMenuListing -> None, FontFamily -> 
          "Helvetica", FontWeight -> "Plain", FontSlant -> "Italic"], 
         Cell[
          StyleData["SB"], StyleMenuListing -> None, FontFamily -> 
          "Helvetica", FontWeight -> "Bold", FontSlant -> "Plain"], 
         Cell[
          StyleData["SBO"], StyleMenuListing -> None, FontFamily -> 
          "Helvetica", FontWeight -> "Bold", FontSlant -> "Italic"], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["SO10"], StyleMenuListing -> None, FontFamily -> 
             "Helvetica", FontSize -> 10, FontWeight -> "Plain", FontSlant -> 
             "Italic"], 
            Cell[
             StyleData["SO10", "Printout"], StyleMenuListing -> None, 
             FontFamily -> "Helvetica", FontSize -> 7, FontWeight -> "Plain", 
             FontSlant -> "Italic"]}, Closed]]}, Closed]], 
      Cell[
       CellGroupData[{
         Cell["Formulas and Programming", "Section"], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["InlineFormula"], CellMargins -> {{10, 4}, {0, 8}}, 
             CellHorizontalScrolling -> True, 
             HyphenationOptions -> {
              "HyphenationCharacter" -> "\[Continuation]"}, LanguageCategory -> 
             "Formula", ScriptLevel -> 1, SingleLetterItalics -> True], 
            Cell[
             StyleData["InlineFormula", "Presentation"], 
             CellMargins -> {{24, 10}, {10, 10}}, LineSpacing -> {1, 5}, 
             FontSize -> 16], 
            Cell[
             StyleData["InlineFormula", "Condensed"], 
             CellMargins -> {{8, 10}, {6, 6}}, LineSpacing -> {1, 1}, 
             FontSize -> 11], 
            Cell[
             StyleData["InlineFormula", "Printout"], 
             CellMargins -> {{2, 0}, {6, 6}}, FontSize -> 10]}, Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["DisplayFormula"], 
             CellMargins -> {{60, Inherited}, {Inherited, Inherited}}, 
             CellHorizontalScrolling -> True, DefaultFormatType -> 
             DefaultInputFormatType, 
             HyphenationOptions -> {
              "HyphenationCharacter" -> "\[Continuation]"}, LanguageCategory -> 
             "Formula", ScriptLevel -> 0, SingleLetterItalics -> True, 
             UnderoverscriptBoxOptions -> {LimitsPositioning -> True}], 
            Cell[
             StyleData["DisplayFormula", "Presentation"], 
             LineSpacing -> {1, 5}, FontSize -> 16], 
            Cell[
             StyleData["DisplayFormula", "Condensed"], LineSpacing -> {1, 1}, 
             FontSize -> 11], 
            Cell[
             StyleData["DisplayFormula", "Printout"], FontSize -> 10]}, 
           Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["Program"], CellFrame -> {{0, 0}, {0.5, 0.5}}, 
             CellMargins -> {{60, 4}, {0, 8}}, CellHorizontalScrolling -> 
             True, Hyphenation -> False, LanguageCategory -> "Formula", 
             ScriptLevel -> 1, FontFamily -> "Courier"], 
            Cell[
             StyleData["Program", "Presentation"], 
             CellMargins -> {{24, 10}, {10, 10}}, LineSpacing -> {1, 5}, 
             FontSize -> 16], 
            Cell[
             StyleData["Program", "Condensed"], 
             CellMargins -> {{8, 10}, {6, 6}}, LineSpacing -> {1, 1}, 
             FontSize -> 11], 
            Cell[
             StyleData["Program", "Printout"], 
             CellMargins -> {{2, 0}, {6, 6}}, FontSize -> 9]}, Closed]]}, 
        Closed]], 
      Cell[
       CellGroupData[{
         Cell["Outline Styles", "Section"], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["Outline1"], CellMargins -> {{60, 10}, {7, 7}}, 
             CellGroupingRules -> {"SectionGrouping", 50}, 
             ParagraphIndent -> -38, CounterIncrements -> "Outline1", 
             FontSize -> 18, FontWeight -> "Bold", 
             CounterBoxOptions -> {CounterFunction :> CapitalRomanNumeral}], 
            Cell[
             StyleData["Outline1", "Printout"], 
             CounterBoxOptions -> {CounterFunction :> CapitalRomanNumeral}]}, 
           Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["Outline2"], CellMargins -> {{90, 10}, {7, 7}}, 
             CellGroupingRules -> {"SectionGrouping", 60}, 
             ParagraphIndent -> -27, CounterIncrements -> "Outline2", 
             FontSize -> 15, FontWeight -> "Bold", 
             CounterBoxOptions -> {CounterFunction :> (Part[
                 CharacterRange["A", "Z"], #]& )}], 
            Cell[
             StyleData["Outline2", "Printout"], 
             CounterBoxOptions -> {CounterFunction :> (Part[
                 CharacterRange["A", "Z"], #]& )}]}, Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["Outline3"], CellMargins -> {{120, 10}, {7, 7}}, 
             CellGroupingRules -> {"SectionGrouping", 70}, 
             ParagraphIndent -> -21, CounterIncrements -> "Outline3", 
             FontSize -> 12, 
             CounterBoxOptions -> {CounterFunction :> Identity}], 
            Cell[
             StyleData["Outline3", "Printout"], 
             CounterBoxOptions -> {CounterFunction :> Identity}]}, Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["Outline4"], CellMargins -> {{150, 10}, {7, 7}}, 
             CellGroupingRules -> {"SectionGrouping", 80}, 
             ParagraphIndent -> -18, CounterIncrements -> "Outline4", 
             FontSize -> 10, CounterBoxOptions -> {CounterFunction :> (Part[
                 CharacterRange["a", "z"], #]& )}], 
            Cell[
             StyleData["Outline4", "Printout"]]}, Closed]]}, Closed]], 
      Cell[
       CellGroupData[{
         Cell["Hyperlink Styles", "Section"], 
         Cell[
         "The cells below define styles useful for making hypertext \
ButtonBoxes.  The \"Hyperlink\" style is for links within the same Notebook, \
or between Notebooks.", "Text"], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["Hyperlink"], StyleMenuListing -> None, 
             ButtonStyleMenuListing -> Automatic, 
             FontVariations -> {"Underline" -> True}, FontColor -> 
             RGBColor[0.269993, 0.308507, 0.6], 
             ButtonBoxOptions -> {
              Active -> True, Appearance -> {Automatic, None}, 
               ButtonFunction :> (FrontEndExecute[{
                  FrontEnd`NotebookLocate[#2]}]& ), ButtonNote -> 
               ButtonData}], 
            Cell[
             StyleData["Hyperlink", "Presentation"], FontSize -> 16], 
            Cell[
             StyleData["Hyperlink", "Condensed"], FontSize -> 11], 
            Cell[
             StyleData["Hyperlink", "Printout"], FontSize -> 10, 
             FontVariations -> {"Underline" -> False}, FontColor -> 
             GrayLevel[0]]}, Closed]], 
         Cell[
         "The following styles are for linking automatically to the on-line \
help system.", "Text"], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["MainBookLink"], StyleMenuListing -> None, 
             ButtonStyleMenuListing -> Automatic, 
             FontVariations -> {"Underline" -> True}, FontColor -> 
             RGBColor[0.269993, 0.308507, 0.6], 
             ButtonBoxOptions -> {
              Active -> True, Appearance -> {Automatic, None}, 
               ButtonFunction :> (FrontEndExecute[{
                  FrontEnd`HelpBrowserLookup["MainBook", #]}]& )}], 
            Cell[
             StyleData["MainBookLink", "Presentation"], FontSize -> 16], 
            Cell[
             StyleData["MainBookLink", "Condensed"], FontSize -> 11], 
            Cell[
             StyleData["MainBookLink", "Printout"], FontSize -> 10, 
             FontVariations -> {"Underline" -> False}, FontColor -> 
             GrayLevel[0]]}, Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["AddOnsLink"], StyleMenuListing -> None, 
             ButtonStyleMenuListing -> Automatic, FontFamily -> "Courier", 
             FontVariations -> {"Underline" -> True}, FontColor -> 
             RGBColor[0.269993, 0.308507, 0.6], 
             ButtonBoxOptions -> {
              Active -> True, Appearance -> {Automatic, None}, 
               ButtonFunction :> (FrontEndExecute[{
                  FrontEnd`HelpBrowserLookup["AddOns", #]}]& )}], 
            Cell[
             StyleData["AddOnsLink", "Presentation"], FontSize -> 16], 
            Cell[
             StyleData["AddOnsLink", "Condensed"], FontSize -> 11], 
            Cell[
             StyleData["AddOnsLink", "Printout"], FontSize -> 10, 
             FontVariations -> {"Underline" -> False}, FontColor -> 
             GrayLevel[0]]}, Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["RefGuideLink"], StyleMenuListing -> None, 
             ButtonStyleMenuListing -> Automatic, FontFamily -> "Courier", 
             FontVariations -> {"Underline" -> True}, FontColor -> 
             RGBColor[0.269993, 0.308507, 0.6], 
             ButtonBoxOptions -> {
              Active -> True, Appearance -> {Automatic, None}, 
               ButtonFunction :> (FrontEndExecute[{
                  FrontEnd`HelpBrowserLookup["RefGuide", #]}]& )}], 
            Cell[
             StyleData["RefGuideLink", "Presentation"], FontSize -> 16], 
            Cell[
             StyleData["RefGuideLink", "Condensed"], FontSize -> 11], 
            Cell[
             StyleData["RefGuideLink", "Printout"], FontSize -> 10, 
             FontVariations -> {"Underline" -> False}, FontColor -> 
             GrayLevel[0]]}, Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["RefGuideLinkText"], StyleMenuListing -> None, 
             ButtonStyleMenuListing -> Automatic, 
             FontVariations -> {"Underline" -> True}, FontColor -> 
             RGBColor[0.269993, 0.308507, 0.6], 
             ButtonBoxOptions -> {
              Active -> True, Appearance -> {Automatic, None}, 
               ButtonFunction :> (FrontEndExecute[{
                  FrontEnd`HelpBrowserLookup["RefGuide", #]}]& )}], 
            Cell[
             StyleData["RefGuideLinkText", "Presentation"], FontSize -> 16], 
            Cell[
             StyleData["RefGuideLinkText", "Condensed"], FontSize -> 11], 
            Cell[
             StyleData["RefGuideLinkText", "Printout"], FontSize -> 10, 
             FontVariations -> {"Underline" -> False}, FontColor -> 
             GrayLevel[0]]}, Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["GettingStartedLink"], StyleMenuListing -> None, 
             ButtonStyleMenuListing -> Automatic, 
             FontVariations -> {"Underline" -> True}, FontColor -> 
             RGBColor[0.269993, 0.308507, 0.6], 
             ButtonBoxOptions -> {
              Active -> True, Appearance -> {Automatic, None}, 
               ButtonFunction :> (FrontEndExecute[{
                  FrontEnd`HelpBrowserLookup["GettingStarted", #]}]& )}], 
            Cell[
             StyleData["GettingStartedLink", "Presentation"], FontSize -> 16], 
            Cell[
             StyleData["GettingStartedLink", "Condensed"], FontSize -> 11], 
            Cell[
             StyleData["GettingStartedLink", "Printout"], FontSize -> 10, 
             FontVariations -> {"Underline" -> False}, FontColor -> 
             GrayLevel[0]]}, Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["DemosLink"], StyleMenuListing -> None, 
             ButtonStyleMenuListing -> Automatic, 
             FontVariations -> {"Underline" -> True}, FontColor -> 
             RGBColor[0.269993, 0.308507, 0.6], 
             ButtonBoxOptions -> {
              Active -> True, Appearance -> {Automatic, None}, 
               ButtonFunction :> (FrontEndExecute[{
                  FrontEnd`HelpBrowserLookup["Demos", #]}]& )}], 
            Cell[
             StyleData["DemosLink", "Printout"], 
             FontVariations -> {"Underline" -> False}, FontColor -> 
             GrayLevel[0]]}, Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["TourLink"], StyleMenuListing -> None, 
             ButtonStyleMenuListing -> Automatic, 
             FontVariations -> {"Underline" -> True}, FontColor -> 
             RGBColor[0.269993, 0.308507, 0.6], 
             ButtonBoxOptions -> {
              Active -> True, Appearance -> {Automatic, None}, 
               ButtonFunction :> (FrontEndExecute[{
                  FrontEnd`HelpBrowserLookup["Tour", #]}]& )}], 
            Cell[
             StyleData["TourLink", "Printout"], 
             FontVariations -> {"Underline" -> False}, FontColor -> 
             GrayLevel[0]]}, Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["OtherInformationLink"], StyleMenuListing -> None, 
             ButtonStyleMenuListing -> Automatic, 
             FontVariations -> {"Underline" -> True}, FontColor -> 
             RGBColor[0.269993, 0.308507, 0.6], 
             ButtonBoxOptions -> {
              Active -> True, Appearance -> {Automatic, None}, 
               ButtonFunction :> (FrontEndExecute[{
                  FrontEnd`HelpBrowserLookup["OtherInformation", #]}]& )}], 
            Cell[
             StyleData["OtherInformationLink", "Presentation"], FontSize -> 
             16], 
            Cell[
             StyleData["OtherInformationLink", "Condensed"], FontSize -> 11], 
            
            Cell[
             StyleData["OtherInformationLink", "Printout"], FontSize -> 10, 
             FontVariations -> {"Underline" -> False}, FontColor -> 
             GrayLevel[0]]}, Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["MasterIndexLink"], StyleMenuListing -> None, 
             ButtonStyleMenuListing -> Automatic, 
             FontVariations -> {"Underline" -> True}, FontColor -> 
             RGBColor[0.269993, 0.308507, 0.6], 
             ButtonBoxOptions -> {
              Active -> True, Appearance -> {Automatic, None}, 
               ButtonFunction :> (FrontEndExecute[{
                  FrontEnd`HelpBrowserLookup["MasterIndex", #]}]& )}], 
            Cell[
             StyleData["MasterIndexLink", "Printout"], 
             FontVariations -> {"Underline" -> False}, FontColor -> 
             GrayLevel[0]]}, Closed]]}, Closed]], 
      Cell[
       CellGroupData[{
         Cell["Styles for Headers and Footers", "Section"], 
         Cell[
          StyleData["Header"], CellMargins -> {{0, 0}, {4, 1}}, 
          DefaultNewInlineCellStyle -> "None", LanguageCategory -> 
          "NaturalLanguage", StyleMenuListing -> None, FontSize -> 10, 
          FontSlant -> "Italic"], 
         Cell[
          StyleData["Footer"], CellMargins -> {{0, 0}, {0, 4}}, 
          DefaultNewInlineCellStyle -> "None", LanguageCategory -> 
          "NaturalLanguage", StyleMenuListing -> None, FontSize -> 9, 
          FontSlant -> "Italic"], 
         Cell[
          StyleData["PageNumber"], CellMargins -> {{0, 0}, {4, 1}}, 
          StyleMenuListing -> None, FontFamily -> "Times", FontSize -> 10]}, 
        Closed]], 
      Cell[
       CellGroupData[{
         Cell["Palette Styles", "Section"], 
         Cell[
         "The cells below define styles that define standard ButtonFunctions, \
for use in palette buttons.", "Text"], 
         Cell[
          StyleData["Paste"], StyleMenuListing -> None, 
          ButtonStyleMenuListing -> Automatic, 
          ButtonBoxOptions -> {ButtonFunction :> (FrontEndExecute[{
               FrontEnd`NotebookApply[
                FrontEnd`InputNotebook[], #, Placeholder]}]& )}], 
         Cell[
          StyleData["Evaluate"], StyleMenuListing -> None, 
          ButtonStyleMenuListing -> Automatic, 
          ButtonBoxOptions -> {ButtonFunction :> (FrontEndExecute[{
               FrontEnd`NotebookApply[
                FrontEnd`InputNotebook[], #, All], 
               SelectionEvaluate[
                FrontEnd`InputNotebook[], All]}]& )}], 
         Cell[
          StyleData["EvaluateCell"], StyleMenuListing -> None, 
          ButtonStyleMenuListing -> Automatic, 
          ButtonBoxOptions -> {ButtonFunction :> (FrontEndExecute[{
               FrontEnd`NotebookApply[
                FrontEnd`InputNotebook[], #, All], 
               FrontEnd`SelectionMove[
                FrontEnd`InputNotebook[], All, Cell, 1], 
               FrontEnd`SelectionEvaluateCreateCell[
                FrontEnd`InputNotebook[], All]}]& )}], 
         Cell[
          StyleData["CopyEvaluate"], StyleMenuListing -> None, 
          ButtonStyleMenuListing -> Automatic, 
          ButtonBoxOptions -> {ButtonFunction :> (FrontEndExecute[{
               FrontEnd`SelectionCreateCell[
                FrontEnd`InputNotebook[], All], 
               FrontEnd`NotebookApply[
                FrontEnd`InputNotebook[], #, All], 
               FrontEnd`SelectionEvaluate[
                FrontEnd`InputNotebook[], All]}]& )}], 
         Cell[
          StyleData["CopyEvaluateCell"], StyleMenuListing -> None, 
          ButtonStyleMenuListing -> Automatic, 
          ButtonBoxOptions -> {ButtonFunction :> (FrontEndExecute[{
               FrontEnd`SelectionCreateCell[
                FrontEnd`InputNotebook[], All], 
               FrontEnd`NotebookApply[
                FrontEnd`InputNotebook[], #, All], 
               FrontEnd`SelectionEvaluateCreateCell[
                FrontEnd`InputNotebook[], All]}]& )}]}, Closed]], 
      Cell[
       CellGroupData[{
         Cell["Placeholder Styles", "Section"], 
         Cell[
         "The cells below define styles useful for making placeholder objects \
in palette templates.", "Text"], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["Placeholder"], Placeholder -> True, StyleMenuListing -> 
             None, FontSlant -> "Italic", FontColor -> 
             RGBColor[0.890623, 0.864698, 0.384756], 
             TagBoxOptions -> {
              Editable -> False, Selectable -> False, StripWrapperBoxes -> 
               False}], 
            Cell[
             StyleData["Placeholder", "Presentation"]], 
            Cell[
             StyleData["Placeholder", "Condensed"]], 
            Cell[
             StyleData["Placeholder", "Printout"]]}, Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["PrimaryPlaceholder"], StyleMenuListing -> None, 
             DrawHighlighted -> True, FontSlant -> "Italic", Background -> 
             RGBColor[0.912505, 0.891798, 0.507774], 
             TagBoxOptions -> {
              Editable -> False, Selectable -> False, StripWrapperBoxes -> 
               False}], 
            Cell[
             StyleData["PrimaryPlaceholder", "Presentation"]], 
            Cell[
             StyleData["PrimaryPlaceholder", "Condensed"]], 
            Cell[
             StyleData["PrimaryPlaceholder", "Printout"]]}, Closed]]}, 
        Closed]], 
      Cell[
       CellGroupData[{
         Cell["FormatType Styles", "Section"], 
         Cell[
         "The cells below define styles that are mixed in with the styles of \
most cells.  If a cell's FormatType matches the name of one of the styles \
defined below, then that style is applied between the cell's style and its \
own options. This is particularly true of Input and Output.", "Text"], 
         Cell[
          StyleData["CellExpression"], PageWidth -> Infinity, 
          CellMargins -> {{6, Inherited}, {Inherited, Inherited}}, 
          ShowCellLabel -> False, ShowSpecialCharacters -> False, 
          AllowInlineCells -> False, Hyphenation -> False, 
          AutoItalicWords -> {}, StyleMenuListing -> None, FontFamily -> 
          "Courier", FontSize -> 12, Background -> GrayLevel[1]], 
         Cell[
          StyleData["InputForm"], InputAutoReplacements -> {}, 
          AllowInlineCells -> False, Hyphenation -> False, StyleMenuListing -> 
          None, FontFamily -> "Courier"], 
         Cell[
          StyleData["OutputForm"], PageWidth -> Infinity, TextAlignment -> 
          Left, LineSpacing -> {0.6, 1}, StyleMenuListing -> None, FontFamily -> 
          "Courier"], 
         Cell[
          StyleData["StandardForm"], 
          InputAutoReplacements -> {
           "->" -> "\[Rule]", ":>" -> "\[RuleDelayed]", "<=" -> 
            "\[LessEqual]", ">=" -> "\[GreaterEqual]", "!=" -> "\[NotEqual]", 
            "==" -> "\[Equal]", Inherited}, 
          "TwoByteSyntaxCharacterAutoReplacement" -> True, 
          LineSpacing -> {1.25, 0}, StyleMenuListing -> None, FontFamily -> 
          "Courier"], 
         Cell[
          StyleData["TraditionalForm"], 
          InputAutoReplacements -> {
           "->" -> "\[Rule]", ":>" -> "\[RuleDelayed]", "<=" -> 
            "\[LessEqual]", ">=" -> "\[GreaterEqual]", "!=" -> "\[NotEqual]", 
            "==" -> "\[Equal]", Inherited}, 
          "TwoByteSyntaxCharacterAutoReplacement" -> True, 
          LineSpacing -> {1.25, 0}, SingleLetterItalics -> True, 
          TraditionalFunctionNotation -> True, DelimiterMatching -> None, 
          StyleMenuListing -> None], 
         Cell[
         "The style defined below is mixed in to any cell that is in an \
inline cell within another.", "Text"], 
         Cell[
          StyleData["InlineCell"], LanguageCategory -> "Formula", ScriptLevel -> 
          1, StyleMenuListing -> None], 
         Cell[
          StyleData["InlineCellEditing"], StyleMenuListing -> None, 
          Background -> RGBColor[0.964706, 0.929412, 0.839216]]}, Closed]], 
      Cell[
       CellGroupData[{
         Cell["Automatic Styles", "Section"], 
         Cell[
         "The cells below define styles that are used to affect the display \
of certain types of objects in typeset expressions.  For example, \
\"UnmatchedBracket\" style defines how unmatched bracket, curly bracket, and \
parenthesis characters are displayed (typically by coloring them to make them \
stand out).", "Text"], 
         Cell[
          StyleData["UnmatchedBracket"], StyleMenuListing -> None, FontColor -> 
          RGBColor[0.760006, 0.330007, 0.8]], 
         Cell[
          StyleData["Completions"], StyleMenuListing -> None, FontFamily -> 
          "Courier"]}, Closed]], 
      Cell[
       CellGroupData[{
         Cell["Styles from HelpBrowser", "Section"], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["MathCaption"], CellFrame -> {{0, 0}, {0, 0.5}}, 
             CellMargins -> {{66, 12}, {2, 24}}, PageBreakBelow -> False, 
             CellFrameMargins -> {{8, 8}, {8, 2}}, CellFrameColor -> 
             GrayLevel[0.700008], CellFrameLabelMargins -> 4, 
             LineSpacing -> {1, 1}, ParagraphSpacing -> {0, 8}, 
             StyleMenuListing -> None, FontColor -> GrayLevel[0.2]], 
            Cell[
             StyleData["MathCaption", "Presentation"], FontSize -> 18], 
            Cell[
             StyleData["MathCaption", "Printout"], 
             CellMargins -> {{39, 0}, {0, 14}}, Hyphenation -> True, FontSize -> 
             9, FontColor -> GrayLevel[0]]}, Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["ObjectName"], ShowCellBracket -> True, 
             CellMargins -> {{66, 4}, {8, 8}}, Evaluatable -> True, 
             CellGroupingRules -> "InputGrouping", PageBreakWithin -> False, 
             GroupPageBreakWithin -> False, CellLabelAutoDelete -> False, 
             CellLabelMargins -> {{14, Inherited}, {Inherited, Inherited}}, 
             DefaultFormatType -> DefaultInputFormatType, 
             ShowSpecialCharacters -> Automatic, 
             "TwoByteSyntaxCharacterAutoReplacement" -> True, 
             HyphenationOptions -> {
              "HyphenationCharacter" -> "\[Continuation]"}, LanguageCategory -> 
             "Mathematica", FormatType -> StandardForm, ShowStringCharacters -> 
             True, NumberMarks -> True, StyleMenuListing -> None, FontWeight -> 
             "Bold"], 
            Cell[
             StyleData["ObjectName", "Presentation"], FontSize -> 18], 
            Cell[
             StyleData["ObjectName", "Printout"], ShowCellBracket -> False, 
             CellMargins -> {{39, 0}, {6, 6}}, FontSize -> 9]}, Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["Usage"], ShowCellBracket -> True, 
             CellMargins -> {{66, 4}, {8, 8}}, Evaluatable -> True, 
             CellGroupingRules -> "InputGrouping", PageBreakWithin -> False, 
             GroupPageBreakWithin -> False, CellLabelAutoDelete -> False, 
             CellLabelMargins -> {{14, Inherited}, {Inherited, Inherited}}, 
             DefaultFormatType -> DefaultInputFormatType, 
             ShowSpecialCharacters -> Automatic, 
             "TwoByteSyntaxCharacterAutoReplacement" -> True, 
             HyphenationOptions -> {
              "HyphenationCharacter" -> "\[Continuation]"}, LanguageCategory -> 
             "Mathematica", FormatType -> StandardForm, ShowStringCharacters -> 
             True, NumberMarks -> True, StyleMenuListing -> None, FontWeight -> 
             "Bold"], 
            Cell[
             StyleData["Usage", "Presentation"], FontSize -> 18], 
            Cell[
             StyleData["Usage", "Printout"], ShowCellBracket -> False, 
             CellMargins -> {{39, 0}, {6, 6}}, FontSize -> 9]}, Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["Notes"], ShowCellBracket -> True, 
             CellMargins -> {{66, 4}, {8, 8}}, Evaluatable -> True, 
             CellGroupingRules -> "InputGrouping", PageBreakWithin -> False, 
             GroupPageBreakWithin -> False, CellLabelAutoDelete -> False, 
             CellLabelMargins -> {{14, Inherited}, {Inherited, Inherited}}, 
             DefaultFormatType -> DefaultInputFormatType, 
             ShowSpecialCharacters -> Automatic, 
             "TwoByteSyntaxCharacterAutoReplacement" -> True, 
             HyphenationOptions -> {
              "HyphenationCharacter" -> "\[Continuation]"}, LanguageCategory -> 
             "Mathematica", FormatType -> StandardForm, ShowStringCharacters -> 
             True, NumberMarks -> True, StyleMenuListing -> None, FontWeight -> 
             "Bold"], 
            Cell[
             StyleData["Notes", "Presentation"], FontSize -> 18], 
            Cell[
             StyleData["Notes", "Printout"], ShowCellBracket -> False, 
             CellMargins -> {{39, 0}, {6, 6}}, FontSize -> 9]}, Closed]], 
         Cell[
          CellGroupData[{
            Cell[
             StyleData["InlineOutput"], ShowCellBracket -> True, 
             CellMargins -> {{66, 4}, {8, 8}}, Evaluatable -> True, 
             CellGroupingRules -> "InputGrouping", PageBreakWithin -> False, 
             GroupPageBreakWithin -> False, CellLabelAutoDelete -> False, 
             CellLabelMargins -> {{14, Inherited}, {Inherited, Inherited}}, 
             DefaultFormatType -> DefaultInputFormatType, 
             ShowSpecialCharacters -> Automatic, 
             "TwoByteSyntaxCharacterAutoReplacement" -> True, 
             HyphenationOptions -> {
              "HyphenationCharacter" -> "\[Continuation]"}, LanguageCategory -> 
             "Mathematica", FormatType -> StandardForm, ShowStringCharacters -> 
             True, NumberMarks -> True, StyleMenuListing -> None, FontWeight -> 
             "Bold"], 
            Cell[
             StyleData["InlineOutput", "Presentation"], FontSize -> 18], 
            Cell[
             StyleData["InlineOutput", "Printout"], ShowCellBracket -> False, 
             CellMargins -> {{39, 0}, {6, 6}}, FontSize -> 9]}, Closed]], 
         Cell[
          CellGroupData[{
            Cell["Emphasis Boxes and Pictures", "Subsection"], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["Box"], CellFrame -> 0.5, 
                CellMargins -> {{27, 12}, {0, 8}}, CellHorizontalScrolling -> 
                True, CellFrameColor -> RGBColor[0.74902, 0.694118, 0.552941],
                 StyleMenuListing -> None, Background -> 
                RGBColor[0.964706, 0.929412, 0.839216], 
                FrameBoxOptions -> {BoxFrame -> 0.5, FrameMargins -> True}, 
                GridBoxOptions -> {GridBoxSpacings -> {"Columns" -> {
                    Offset[0.27999999999999997`], {
                    Offset[0.7]}, 
                    Offset[0.27999999999999997`]}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {
                    Offset[0.2], {
                    Offset[0.4]}, 
                    Offset[0.2]}, "RowsIndexed" -> {}}}], 
               Cell[
                StyleData["Box", "Presentation"], FontSize -> 18], 
               Cell[
                StyleData["Box", "Printout"], CellMargins -> {{2, 0}, {0, 8}},
                 FontSize -> 10, Background -> GrayLevel[0.900008]]}, 
              Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["DoubleBox"], CellFrame -> 0.5, 
                CellMargins -> {{27, 12}, {0, 8}}, CellHorizontalScrolling -> 
                True, CellFrameColor -> RGBColor[0.74902, 0.694118, 0.552941],
                 StyleMenuListing -> None, Background -> 
                RGBColor[0.964706, 0.929412, 0.839216], 
                FrameBoxOptions -> {BoxFrame -> 0.5, FrameMargins -> True}, 
                GridBoxOptions -> {
                 GridBoxAlignment -> {
                   "Columns" -> {{Center}}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {{Top}}, "RowsIndexed" -> {}}, 
                  GridBoxSpacings -> {"Columns" -> {
                    Offset[0.27999999999999997`], {
                    Offset[1.4]}, 
                    Offset[0.27999999999999997`]}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {
                    Offset[0.2], {
                    Offset[0.4]}, 
                    Offset[0.2]}, "RowsIndexed" -> {}}}], 
               Cell[
                StyleData["DoubleBox", "Presentation"], FontSize -> 18], 
               Cell[
                StyleData["DoubleBox", "Printout"], 
                CellMargins -> {{2, 0}, {0, 8}}, FontSize -> 10, Background -> 
                GrayLevel[0.900008]]}, Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["1ColumnBox"], CellFrame -> 0.5, 
                CellMargins -> {{27, 12}, {0, 8}}, CellHorizontalScrolling -> 
                True, CellFrameColor -> RGBColor[0.74902, 0.694118, 0.552941],
                 LineIndent -> 0, StyleMenuListing -> None, Background -> 
                RGBColor[0.964706, 0.929412, 0.839216], 
                FrameBoxOptions -> {BoxFrame -> 0.5, FrameMargins -> True}, 
                GridBoxOptions -> {GridBoxSpacings -> {"Columns" -> {
                    Offset[0.27999999999999997`], {
                    Offset[0.7]}, 
                    Offset[0.27999999999999997`]}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {
                    Offset[0.2], {
                    Offset[0.4]}, 
                    Offset[0.2]}, "RowsIndexed" -> {}}}], 
               Cell[
                StyleData["1ColumnBox", "Presentation"], FontSize -> 18], 
               Cell[
                StyleData["1ColumnBox", "Printout"], 
                CellMargins -> {{2, 0}, {0, 8}}, FontSize -> 10, Background -> 
                GrayLevel[0.900008]]}, Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["2ColumnBox"], CellFrame -> 0.5, 
                CellMargins -> {{27, 12}, {0, 8}}, CellHorizontalScrolling -> 
                True, CellFrameColor -> RGBColor[0.74902, 0.694118, 0.552941],
                 SingleLetterItalics -> False, LineIndent -> 0, 
                StyleMenuListing -> None, Background -> 
                RGBColor[0.964706, 0.929412, 0.839216], 
                FrameBoxOptions -> {BoxFrame -> 0.5, FrameMargins -> True}, 
                GridBoxOptions -> {GridBoxItemSize -> {"Columns" -> {
                    Scaled[0.31], {
                    Scaled[0.67]}}, "ColumnsIndexed" -> {}, "Rows" -> {{1.}}, 
                    "RowsIndexed" -> {}}}], 
               Cell[
                StyleData["2ColumnBox", "Presentation"], FontSize -> 18], 
               Cell[
                StyleData["2ColumnBox", "Printout"], 
                CellMargins -> {{2, 0}, {0, 8}}, FontSize -> 9, Background -> 
                GrayLevel[0.900008]]}, Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["2ColumnEvenBox"], CellFrame -> 0.5, 
                CellMargins -> {{27, 12}, {0, 8}}, CellHorizontalScrolling -> 
                True, CellFrameColor -> RGBColor[0.74902, 0.694118, 0.552941],
                 LineIndent -> 0, StyleMenuListing -> None, Background -> 
                RGBColor[0.964706, 0.929412, 0.839216], 
                FrameBoxOptions -> {BoxFrame -> 0.5, FrameMargins -> True}, 
                GridBoxOptions -> {GridBoxItemSize -> {"Columns" -> {{
                    Scaled[0.46]}}, "ColumnsIndexed" -> {}, "Rows" -> {{1.}}, 
                    "RowsIndexed" -> {}}}], 
               Cell[
                StyleData["2ColumnEvenBox", "Presentation"], FontSize -> 18], 
               
               Cell[
                StyleData["2ColumnEvenBox", "Printout"], 
                CellMargins -> {{2, 0}, {0, 8}}, FontSize -> 10, Background -> 
                GrayLevel[0.900008]]}, Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["2ColumnSmallBox"], CellFrame -> 0.5, 
                CellMargins -> {{27, 12}, {0, 8}}, CellHorizontalScrolling -> 
                True, CellFrameColor -> RGBColor[0.74902, 0.694118, 0.552941],
                 LineIndent -> 0, StyleMenuListing -> None, Background -> 
                RGBColor[0.964706, 0.929412, 0.839216], 
                FrameBoxOptions -> {BoxFrame -> 0.5, FrameMargins -> True}, 
                GridBoxOptions -> {
                 GridBoxAlignment -> {
                   "Columns" -> {Right, {Left}}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {{Baseline}}, "RowsIndexed" -> {}}, 
                  GridBoxItemSize -> {"Columns" -> {{
                    Scaled[0.35]}}, "ColumnsIndexed" -> {}, "Rows" -> {{1.}}, 
                    "RowsIndexed" -> {}}, GridBoxSpacings -> {"Columns" -> {
                    Offset[0.27999999999999997`], {
                    Offset[1.0499999999999998`]}, 
                    Offset[0.27999999999999997`]}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {
                    Offset[0.2], {
                    Offset[0.4]}, 
                    Offset[0.2]}, "RowsIndexed" -> {}}}], 
               Cell[
                StyleData["2ColumnSmallBox", "Presentation"], FontSize -> 18], 
               Cell[
                StyleData["2ColumnSmallBox", "Printout"], 
                CellMargins -> {{2, 0}, {0, 8}}, FontSize -> 10, Background -> 
                GrayLevel[0.900008]]}, Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["3ColumnBox"], CellFrame -> 0.5, 
                CellMargins -> {{27, 12}, {0, 8}}, CellHorizontalScrolling -> 
                True, CellFrameColor -> RGBColor[0.74902, 0.694118, 0.552941],
                 LineIndent -> 0, StyleMenuListing -> None, Background -> 
                RGBColor[0.964706, 0.929412, 0.839216], 
                FrameBoxOptions -> {BoxFrame -> 0.5, FrameMargins -> True}, 
                GridBoxOptions -> {GridBoxItemSize -> {"Columns" -> {{
                    Scaled[0.32]}}, "ColumnsIndexed" -> {}, "Rows" -> {{1.}}, 
                    "RowsIndexed" -> {}}}], 
               Cell[
                StyleData["3ColumnBox", "Presentation"], FontSize -> 18], 
               Cell[
                StyleData["3ColumnBox", "Printout"], 
                CellMargins -> {{2, 0}, {0, 8}}, FontSize -> 10, Background -> 
                GrayLevel[0.900008]]}, Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["3ColumnSmallBox"], CellFrame -> 0.5, 
                CellMargins -> {{27, 12}, {0, 8}}, CellHorizontalScrolling -> 
                True, CellFrameColor -> RGBColor[0.74902, 0.694118, 0.552941],
                 LineIndent -> 0, StyleMenuListing -> None, Background -> 
                RGBColor[0.964706, 0.929412, 0.839216], 
                FrameBoxOptions -> {BoxFrame -> 0.5, FrameMargins -> True}, 
                GridBoxOptions -> {
                 GridBoxAlignment -> {
                   "Columns" -> {Right, Center, {Left}}, 
                    "ColumnsIndexed" -> {}, "Rows" -> {{Baseline}}, 
                    "RowsIndexed" -> {}}, GridBoxItemSize -> {"Columns" -> {{
                    Scaled[0.24]}}, "ColumnsIndexed" -> {}, "Rows" -> {{1.}}, 
                    "RowsIndexed" -> {}}, GridBoxSpacings -> {"Columns" -> {
                    Offset[0.27999999999999997`], {
                    Offset[1.0499999999999998`]}, 
                    Offset[0.27999999999999997`]}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {
                    Offset[0.2], {
                    Offset[0.4]}, 
                    Offset[0.2]}, "RowsIndexed" -> {}}}], 
               Cell[
                StyleData["3ColumnSmallBox", "Presentation"], FontSize -> 18], 
               Cell[
                StyleData["3ColumnSmallBox", "Printout"], 
                CellMargins -> {{2, 0}, {0, 8}}, FontSize -> 10, Background -> 
                GrayLevel[0.900008]]}, Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["4ColumnBox"], CellFrame -> 0.5, 
                CellMargins -> {{27, 12}, {0, 8}}, CellHorizontalScrolling -> 
                True, CellFrameColor -> RGBColor[0.74902, 0.694118, 0.552941],
                 SingleLetterItalics -> False, LineIndent -> 0, 
                StyleMenuListing -> None, Background -> 
                RGBColor[0.964706, 0.929412, 0.839216], 
                FrameBoxOptions -> {BoxFrame -> 0.5, FrameMargins -> True}, 
                GridBoxOptions -> {GridBoxItemSize -> {"Columns" -> {
                    Scaled[0.13], 
                    Scaled[0.35], 
                    Scaled[0.13], {
                    Scaled[0.35]}}, "ColumnsIndexed" -> {}, "Rows" -> {{1.}}, 
                    "RowsIndexed" -> {}}}], 
               Cell[
                StyleData["4ColumnBox", "Presentation"], FontSize -> 18], 
               Cell[
                StyleData["4ColumnBox", "Printout"], 
                CellMargins -> {{2, 0}, {0, 8}}, FontSize -> 10, Background -> 
                GrayLevel[0.900008]]}, Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["5ColumnBox"], CellFrame -> 0.5, 
                CellMargins -> {{27, 12}, {0, 8}}, CellHorizontalScrolling -> 
                True, CellFrameColor -> RGBColor[0.74902, 0.694118, 0.552941],
                 LineIndent -> 0, StyleMenuListing -> None, Background -> 
                RGBColor[0.964706, 0.929412, 0.839216], 
                FrameBoxOptions -> {BoxFrame -> 0.5, FrameMargins -> True}, 
                GridBoxOptions -> {GridBoxItemSize -> {"Columns" -> {{
                    Scaled[0.202]}}, "ColumnsIndexed" -> {}, "Rows" -> {{1.}},
                     "RowsIndexed" -> {}}}], 
               Cell[
                StyleData["5ColumnBox", "Presentation"], FontSize -> 18], 
               Cell[
                StyleData["5ColumnBox", "Printout"], 
                CellMargins -> {{2, 0}, {0, 8}}, FontSize -> 9, Background -> 
                GrayLevel[0.900008]]}, Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["6ColumnBox"], CellFrame -> 0.5, 
                CellMargins -> {{27, 12}, {0, 8}}, CellHorizontalScrolling -> 
                True, CellFrameColor -> RGBColor[0.74902, 0.694118, 0.552941],
                 LineIndent -> 0, StyleMenuListing -> None, Background -> 
                RGBColor[0.964706, 0.929412, 0.839216], 
                FrameBoxOptions -> {BoxFrame -> 0.5, FrameMargins -> True}, 
                GridBoxOptions -> {GridBoxItemSize -> {"Columns" -> {
                    Scaled[0.12], 
                    Scaled[0.22], 
                    Scaled[0.12], 
                    Scaled[0.12], 
                    Scaled[0.22], {
                    Scaled[0.12]}}, "ColumnsIndexed" -> {}, "Rows" -> {{1.}}, 
                    "RowsIndexed" -> {}}}], 
               Cell[
                StyleData["6ColumnBox", "Presentation"], FontSize -> 18], 
               Cell[
                StyleData["6ColumnBox", "Printout"], 
                CellMargins -> {{2, 0}, {0, 8}}, FontSize -> 10, Background -> 
                GrayLevel[0.900008]]}, Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["FramedBox"], CellFrame -> 0.5, 
                CellMargins -> {{27, 12}, {0, 8}}, CellHorizontalScrolling -> 
                True, PageBreakWithin -> False, CellFrameColor -> 
                RGBColor[0.74902, 0.694118, 0.552941], AutoIndent -> False, 
                AutoSpacing -> False, LineIndent -> 0, StyleMenuListing -> 
                None, FontWeight -> "Plain", Background -> 
                RGBColor[0.964706, 0.929412, 0.839216], 
                GridBoxOptions -> {
                 GridBoxAlignment -> {
                   "Columns" -> {{Left}}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {{Baseline}}, "RowsIndexed" -> {}}, 
                  GridBoxSpacings -> {"Columns" -> {
                    Offset[0.27999999999999997`], {
                    Offset[0.5599999999999999]}, 
                    Offset[0.27999999999999997`]}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {
                    Offset[0.2], {
                    Offset[0.6]}, 
                    Offset[0.2]}, "RowsIndexed" -> {}}}], 
               Cell[
                StyleData["FramedBox", "Presentation"], FontSize -> 18], 
               Cell[
                StyleData["FramedBox", "Printout"], 
                CellMargins -> {{2, 4}, {0, 8}}, FontSize -> 10, Background -> 
                GrayLevel[1]]}, Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["DefinitionBox"], CellFrame -> 0.5, 
                CellMargins -> {{27, 12}, {0, 8}}, CellHorizontalScrolling -> 
                True, PageBreakWithin -> False, CellFrameColor -> 
                RGBColor[0.74902, 0.694118, 0.552941], AutoIndent -> False, 
                AutoSpacing -> False, LineIndent -> 0, StyleMenuListing -> 
                None, FontWeight -> "Plain", Background -> 
                RGBColor[0.964706, 0.929412, 0.839216], 
                GridBoxOptions -> {
                 GridBoxAlignment -> {
                   "Columns" -> {{Left}}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {{Baseline}}, "RowsIndexed" -> {}}, 
                  GridBoxItemSize -> {"Columns" -> {
                    Scaled[0.4], {
                    Scaled[0.6]}}, "ColumnsIndexed" -> {}, "Rows" -> {{1.}}, 
                    "RowsIndexed" -> {}}, GridBoxSpacings -> {"Columns" -> {
                    Offset[0.27999999999999997`], {
                    Offset[0.7]}, 
                    Offset[0.27999999999999997`]}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {
                    Offset[0.2], {
                    Offset[0.6]}, 
                    Offset[0.2]}, "RowsIndexed" -> {}}}], 
               Cell[
                StyleData["DefinitionBox", "Presentation"], FontSize -> 18], 
               Cell[
                StyleData["DefinitionBox", "Printout"], 
                CellMargins -> {{2, 4}, {0, 8}}, FontSize -> 10, Background -> 
                GrayLevel[1]]}, Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["DefinitionBox3Col"], CellFrame -> 0.5, 
                CellMargins -> {{27, 12}, {0, 8}}, CellHorizontalScrolling -> 
                True, PageBreakWithin -> False, CellFrameColor -> 
                RGBColor[0.74902, 0.694118, 0.552941], AutoIndent -> False, 
                AutoSpacing -> False, LineIndent -> 0, StyleMenuListing -> 
                None, FontWeight -> "Plain", Background -> 
                RGBColor[0.964706, 0.929412, 0.839216], 
                GridBoxOptions -> {
                 GridBoxAlignment -> {
                   "Columns" -> {{Left}}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {{Baseline}}, "RowsIndexed" -> {}}, 
                  GridBoxItemSize -> {"Columns" -> {
                    Scaled[0.35], 
                    Scaled[0.2], {
                    Scaled[0.45]}}, "ColumnsIndexed" -> {}, "Rows" -> {{1.}}, 
                    "RowsIndexed" -> {}}, GridBoxSpacings -> {"Columns" -> {
                    Offset[0.27999999999999997`], {
                    Offset[0.7]}, 
                    Offset[0.27999999999999997`]}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {
                    Offset[0.2], {
                    Offset[0.6]}, 
                    Offset[0.2]}, "RowsIndexed" -> {}}}], 
               Cell[
                StyleData["DefinitionBox3Col", "Presentation"], FontSize -> 
                18], 
               Cell[
                StyleData["DefinitionBox3Col", "Printout"], 
                CellMargins -> {{2, 4}, {0, 8}}, FontSize -> 10, Background -> 
                GrayLevel[1]]}, Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["DefinitionBox4Col"], CellFrame -> 0.5, 
                CellMargins -> {{27, 12}, {0, 8}}, CellHorizontalScrolling -> 
                True, PageBreakWithin -> False, CellFrameColor -> 
                RGBColor[0.74902, 0.694118, 0.552941], AutoIndent -> False, 
                AutoSpacing -> False, LineIndent -> 0, StyleMenuListing -> 
                None, FontWeight -> "Plain", Background -> 
                RGBColor[0.964706, 0.929412, 0.839216], 
                GridBoxOptions -> {
                 GridBoxAlignment -> {
                   "Columns" -> {{Left}}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {{Baseline}}, "RowsIndexed" -> {}}, 
                  GridBoxItemSize -> {"Columns" -> {
                    Scaled[0.15], 
                    Scaled[0.35], 
                    Scaled[0.15], {
                    Scaled[0.35]}}, "ColumnsIndexed" -> {}, "Rows" -> {{1.}}, 
                    "RowsIndexed" -> {}}, GridBoxSpacings -> {"Columns" -> {
                    Offset[0.27999999999999997`], {
                    Offset[0.7]}, 
                    Offset[0.27999999999999997`]}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {
                    Offset[0.2], {
                    Offset[0.6]}, 
                    Offset[0.2]}, "RowsIndexed" -> {}}}], 
               Cell[
                StyleData["DefinitionBox4Col", "Presentation"], FontSize -> 
                18], 
               Cell[
                StyleData["DefinitionBox4Col", "Printout"], 
                CellMargins -> {{2, 4}, {0, 8}}, FontSize -> 10, Background -> 
                GrayLevel[1]]}, Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["DefinitionBox5Col"], CellFrame -> 0.5, 
                CellMargins -> {{27, 12}, {0, 8}}, CellHorizontalScrolling -> 
                True, PageBreakWithin -> False, CellFrameColor -> 
                RGBColor[0.74902, 0.694118, 0.552941], AutoIndent -> False, 
                AutoSpacing -> False, LineIndent -> 0, StyleMenuListing -> 
                None, FontWeight -> "Plain", Background -> 
                RGBColor[0.964706, 0.929412, 0.839216], 
                GridBoxOptions -> {
                 GridBoxAlignment -> {
                   "Columns" -> {{Left}}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {{Baseline}}, "RowsIndexed" -> {}}, 
                  GridBoxItemSize -> {"Columns" -> {{
                    Scaled[0.2]}}, "ColumnsIndexed" -> {}, "Rows" -> {{1.}}, 
                    "RowsIndexed" -> {}}, GridBoxSpacings -> {"Columns" -> {
                    Offset[0.27999999999999997`], {
                    Offset[0.7]}, 
                    Offset[0.27999999999999997`]}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {
                    Offset[0.2], {
                    Offset[0.6]}, 
                    Offset[0.2]}, "RowsIndexed" -> {}}}], 
               Cell[
                StyleData["DefinitionBox5Col", "Presentation"], FontSize -> 
                18], 
               Cell[
                StyleData["DefinitionBox5Col", "Printout"], 
                CellMargins -> {{2, 4}, {0, 8}}, FontSize -> 10, Background -> 
                GrayLevel[1]]}, Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["DefinitionBox6Col"], CellFrame -> 0.5, 
                CellMargins -> {{27, 12}, {0, 8}}, CellHorizontalScrolling -> 
                True, PageBreakWithin -> False, CellFrameColor -> 
                RGBColor[0.74902, 0.694118, 0.552941], AutoIndent -> False, 
                AutoSpacing -> False, LineIndent -> 0, StyleMenuListing -> 
                None, FontWeight -> "Plain", Background -> 
                RGBColor[0.964706, 0.929412, 0.839216], 
                GridBoxOptions -> {
                 GridBoxAlignment -> {
                   "Columns" -> {{Left}}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {{Baseline}}, "RowsIndexed" -> {}}, 
                  GridBoxItemSize -> {"Columns" -> {
                    Scaled[0.13], 
                    Scaled[0.24], 
                    Scaled[0.13], 
                    Scaled[0.13], 
                    Scaled[0.24], {
                    Scaled[0.13]}}, "ColumnsIndexed" -> {}, "Rows" -> {{1.}}, 
                    "RowsIndexed" -> {}}, GridBoxSpacings -> {"Columns" -> {
                    Offset[0.27999999999999997`], {
                    Offset[0.7]}, 
                    Offset[0.27999999999999997`]}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {
                    Offset[0.2], {
                    Offset[0.6]}, 
                    Offset[0.2]}, "RowsIndexed" -> {}}}], 
               Cell[
                StyleData["DefinitionBox6Col", "Presentation"], FontSize -> 
                18], 
               Cell[
                StyleData["DefinitionBox6Col", "Printout"], 
                CellMargins -> {{2, 4}, {0, 8}}, FontSize -> 10, Background -> 
                GrayLevel[1]]}, Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["TopBox"], CellFrame -> {{0.5, 0.5}, {0, 0.5}}, 
                CellMargins -> {{27, 12}, {0, 8}}, CellHorizontalScrolling -> 
                True, PageBreakBelow -> False, CellFrameColor -> 
                RGBColor[0.74902, 0.694118, 0.552941], AutoIndent -> False, 
                AutoSpacing -> False, LineIndent -> 0, StyleMenuListing -> 
                None, FontWeight -> "Plain", Background -> 
                RGBColor[0.964706, 0.929412, 0.839216], 
                GridBoxOptions -> {
                 GridBoxAlignment -> {
                   "Columns" -> {{Left}}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {{Baseline}}, "RowsIndexed" -> {}}, 
                  GridBoxItemSize -> {"Columns" -> {
                    Scaled[0.31], {
                    Scaled[0.62]}}, "ColumnsIndexed" -> {}, "Rows" -> {{1.}}, 
                    "RowsIndexed" -> {}}, GridBoxSpacings -> {"Columns" -> {
                    Offset[0.27999999999999997`], {
                    Offset[0.7]}, 
                    Offset[0.27999999999999997`]}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {
                    Offset[0.2], {
                    Offset[0.6]}, 
                    Offset[0.2]}, "RowsIndexed" -> {}}}], 
               Cell[
                StyleData["TopBox", "Presentation"], FontSize -> 18], 
               Cell[
                StyleData["TopBox", "Printout"], 
                CellMargins -> {{2, 0}, {0, 8}}, Background -> GrayLevel[1]]},
               Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["MiddleBox"], CellFrame -> {{0.5, 0.5}, {0, 0}}, 
                CellMargins -> {{27, 12}, {0, -7}}, CellHorizontalScrolling -> 
                True, PageBreakAbove -> False, PageBreakBelow -> False, 
                CellFrameColor -> RGBColor[0.74902, 0.694118, 0.552941], 
                AutoIndent -> False, AutoSpacing -> False, LineIndent -> 0, 
                StyleMenuListing -> None, FontWeight -> "Plain", Background -> 
                RGBColor[0.964706, 0.929412, 0.839216], 
                GridBoxOptions -> {
                 GridBoxAlignment -> {
                   "Columns" -> {{Left}}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {{Baseline}}, "RowsIndexed" -> {}}, 
                  GridBoxItemSize -> {"Columns" -> {
                    Scaled[0.31], {
                    Scaled[0.62]}}, "ColumnsIndexed" -> {}, "Rows" -> {{1.}}, 
                    "RowsIndexed" -> {}}, GridBoxSpacings -> {"Columns" -> {
                    Offset[0.27999999999999997`], {
                    Offset[0.7]}, 
                    Offset[0.27999999999999997`]}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {
                    Offset[0.2], {
                    Offset[0.6]}, 
                    Offset[0.2]}, "RowsIndexed" -> {}}}], 
               Cell[
                StyleData["MiddleBox", "Presentation"], FontSize -> 18], 
               Cell[
                StyleData["MiddleBox", "Printout"], 
                CellMargins -> {{2, 0}, {0, 2}}, Background -> GrayLevel[1]]},
               Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["BottomBox"], CellFrame -> {{0.5, 0.5}, {0.5, 0}}, 
                CellMargins -> {{27, 12}, {0, -7}}, CellHorizontalScrolling -> 
                True, PageBreakAbove -> False, PageBreakBelow -> False, 
                CellFrameColor -> RGBColor[0.74902, 0.694118, 0.552941], 
                AutoIndent -> False, AutoSpacing -> False, LineIndent -> 0, 
                StyleMenuListing -> None, FontWeight -> "Plain", Background -> 
                RGBColor[0.964706, 0.929412, 0.839216], 
                GridBoxOptions -> {
                 GridBoxAlignment -> {
                   "Columns" -> {{Left}}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {{Baseline}}, "RowsIndexed" -> {}}, 
                  GridBoxItemSize -> {"Columns" -> {
                    Scaled[0.31], {
                    Scaled[0.62]}}, "ColumnsIndexed" -> {}, "Rows" -> {{1.}}, 
                    "RowsIndexed" -> {}}, GridBoxSpacings -> {"Columns" -> {
                    Offset[0.27999999999999997`], {
                    Offset[0.7]}, 
                    Offset[0.27999999999999997`]}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {
                    Offset[0.2], {
                    Offset[0.6]}, 
                    Offset[0.2]}, "RowsIndexed" -> {}}}], 
               Cell[
                StyleData["BottomBox", "Presentation"], FontSize -> 18], 
               Cell[
                StyleData["BottomBox", "Printout"], 
                CellMargins -> {{2, 0}, {0, -5}}, FontSize -> 10, Background -> 
                GrayLevel[1], 
                GridBoxOptions -> {
                 GridBoxItemSize -> {
                   "Columns" -> {{All}}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {{2.2}}, "RowsIndexed" -> {}}}]}, Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["TopSpanBox"], CellFrame -> {{0.5, 0.5}, {0, 0.5}}, 
                CellMargins -> {{27, 12}, {-2, 8}}, CellHorizontalScrolling -> 
                True, PageBreakBelow -> False, CellFrameColor -> 
                RGBColor[0.74902, 0.694118, 0.552941], AutoIndent -> False, 
                AutoSpacing -> False, LineIndent -> 0, StyleMenuListing -> 
                None, FontWeight -> "Plain", Background -> 
                RGBColor[0.964706, 0.929412, 0.839216], 
                GridBoxOptions -> {
                 GridBoxAlignment -> {
                   "Columns" -> {{Left}}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {{Baseline}}, "RowsIndexed" -> {}}, 
                  GridBoxItemSize -> {"Columns" -> {
                    Scaled[0.9], {
                    Scaled[0.03]}}, "ColumnsIndexed" -> {}, "Rows" -> {{1.}}, 
                    "RowsIndexed" -> {}}, GridBoxSpacings -> {"Columns" -> {
                    Offset[0.27999999999999997`], {
                    Offset[0.7]}, 
                    Offset[0.27999999999999997`]}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {
                    Offset[0.2], {
                    Offset[0.6]}, 
                    Offset[0.2]}, "RowsIndexed" -> {}}}], 
               Cell[
                StyleData["TopSpanBox", "Presentation"], FontSize -> 18], 
               Cell[
                StyleData["TopSpanBox", "Printout"], 
                CellMargins -> {{2, 0}, {-2, 8}}, FontSize -> 10, Background -> 
                GrayLevel[1]]}, Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["MiddleSpanBox"], CellFrame -> {{0.5, 0.5}, {0, 0}},
                 CellMargins -> {{27, 12}, {0, 0}}, CellHorizontalScrolling -> 
                True, PageBreakAbove -> False, PageBreakBelow -> False, 
                CellFrameColor -> RGBColor[0.74902, 0.694118, 0.552941], 
                AutoIndent -> False, AutoSpacing -> False, LineIndent -> 0, 
                StyleMenuListing -> None, FontWeight -> "Plain", Background -> 
                RGBColor[0.964706, 0.929412, 0.839216], 
                GridBoxOptions -> {
                 GridBoxAlignment -> {
                   "Columns" -> {{Left}}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {{Baseline}}, "RowsIndexed" -> {}}, 
                  GridBoxItemSize -> {"Columns" -> {
                    Scaled[0.9], {
                    Scaled[0.03]}}, "ColumnsIndexed" -> {}, "Rows" -> {{1.}}, 
                    "RowsIndexed" -> {}}, GridBoxSpacings -> {"Columns" -> {
                    Offset[0.27999999999999997`], {
                    Offset[0.7]}, 
                    Offset[0.27999999999999997`]}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {
                    Offset[0.2], {
                    Offset[0.6]}, 
                    Offset[0.2]}, "RowsIndexed" -> {}}}], 
               Cell[
                StyleData["MiddleSpanBox", "Presentation"], FontSize -> 18], 
               Cell[
                StyleData["MiddleSpanBox", "Printout"], 
                CellMargins -> {{2, 0}, {-5, 0}}, FontSize -> 10, Background -> 
                GrayLevel[1], 
                GridBoxOptions -> {
                 GridBoxItemSize -> {
                   "Columns" -> {{All}}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {{1.8}}, "RowsIndexed" -> {}}}]}, Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["Picture"], 
                CellMargins -> {{27, Inherited}, {4, 4}}, CellGroupingRules -> 
                "GraphicsGrouping", CellHorizontalScrolling -> True, 
                StyleMenuListing -> None], 
               Cell[
                StyleData["Picture", "Presentation"], FontSize -> 18], 
               Cell[
                StyleData["Picture", "Printout"], 
                CellMargins -> {{2, Inherited}, {4, 4}}, Magnification -> 
                0.65]}, Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["OpenCloseItemizedPicture"], 
                CellMargins -> {{88, 4}, {4, 4}}, 
                PrivateCellOptions -> {"DefaultCellGroupOpen" -> False}, 
                CellGroupingRules -> "GraphicsGrouping", 
                CellHorizontalScrolling -> True, StyleMenuListing -> None], 
               Cell[
                StyleData["OpenCloseItemizedPicture", "Presentation"], 
                FontSize -> 18], 
               Cell[
                StyleData["OpenCloseItemizedPicture", "Printout"], 
                CellMargins -> {{76, 2}, {0, 0}}, 
                CellElementSpacings -> {
                 "CellMinHeight" -> 1, "ClosedCellHeight" -> 0}, CellOpen -> 
                False]}, Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["ItemizedPicture"], 
                CellMargins -> {{88, 4}, {4, 4}}, CellGroupingRules -> 
                "GraphicsGrouping", CellHorizontalScrolling -> True, 
                StyleMenuListing -> None], 
               Cell[
                StyleData["ItemizedPicture", "Presentation"], FontSize -> 18], 
               Cell[
                StyleData["ItemizedPicture", "Printout"], 
                CellMargins -> {{77, 2}, {4, -4}}, Magnification -> 0.5]}, 
              Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["ListGraphic"], CellMargins -> {{88, 4}, {4, 4}}, 
                CellGroupingRules -> "GraphicsGrouping", 
                CellHorizontalScrolling -> True, StyleMenuListing -> None], 
               Cell[
                StyleData["ListGraphic", "Presentation"], FontSize -> 18], 
               Cell[
                StyleData["ListGraphic", "Printout"], 
                CellMargins -> {{77, 2}, {4, -4}}, Magnification -> 0.5]}, 
              Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["ListNoteBox"], CellFrame -> 0.5, 
                CellMargins -> {{88, 12}, {8, 8}}, CellHorizontalScrolling -> 
                True, CellFrameColor -> RGBColor[0.74902, 0.694118, 0.552941],
                 LineIndent -> 0, StyleMenuListing -> None, Background -> 
                RGBColor[0.964706, 0.929412, 0.839216], 
                FrameBoxOptions -> {FrameMargins -> {{1, 1}, {1.5, 1.5}}}, 
                GridBoxOptions -> {GridBoxSpacings -> {"Columns" -> {
                    Offset[0.27999999999999997`], {
                    Offset[0.7]}, 
                    Offset[0.27999999999999997`]}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {
                    Offset[0.2], {
                    Offset[0.4]}, 
                    Offset[0.2]}, "RowsIndexed" -> {}}}], 
               Cell[
                StyleData["ListNoteBox", "Presentation"], FontSize -> 18], 
               Cell[
                StyleData["ListNoteBox", "Printout"], 
                CellMargins -> {{77, 4}, {6, 2}}, FontSize -> 10, Background -> 
                GrayLevel[0.900008]]}, Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["PictureGroup"], CellMargins -> {{41, 4}, {0, 4}}, 
                CellGroupingRules -> "GraphicsGrouping", 
                CellHorizontalScrolling -> True, StyleMenuListing -> None], 
               Cell[
                StyleData["PictureGroup", "Presentation"], FontSize -> 18], 
               Cell[
                StyleData["PictureGroup", "Printout"], 
                CellMargins -> {{76, 2}, {0, 0}}, 
                CellElementSpacings -> {
                 "CellMinHeight" -> 1, "ClosedCellHeight" -> 0}, CellOpen -> 
                False]}, Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["Sound"], ShowCellBracket -> True, 
                CellMargins -> {{27, Inherited}, {0, 8}}, StyleMenuListing -> 
                None], 
               Cell[
                StyleData["Sound", "Presentation"], FontSize -> 18], 
               Cell[
                StyleData["Sound", "Printout"], 
                CellMargins -> {{2, 0}, {0, 8}}, FontSize -> 10]}, Closed]]}, 
           Closed]], 
         Cell[
          CellGroupData[{
            Cell["Tables", "Subsection"], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["2ColumnTable"], CellMargins -> {{35, 4}, {0, 8}}, 
                CellHorizontalScrolling -> True, LineIndent -> 0, 
                StyleMenuListing -> None, 
                GridBoxOptions -> {
                 GridBoxAlignment -> {
                   "Columns" -> {{Left}}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {{Baseline}}, "RowsIndexed" -> {}}, 
                  GridBoxItemSize -> {"Columns" -> {
                    Scaled[0.34], {
                    Scaled[0.64]}}, "ColumnsIndexed" -> {}, "Rows" -> {{1.}}, 
                    "RowsIndexed" -> {}}}], 
               Cell[
                StyleData["2ColumnTable", "Presentation"], FontSize -> 18], 
               Cell[
                StyleData["2ColumnTable", "Printout"], 
                CellMargins -> {{2, 0}, {0, 8}}, FontSize -> 9]}, Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["2ColumnEvenTable"], 
                CellMargins -> {{35, 4}, {0, 8}}, CellHorizontalScrolling -> 
                True, LineIndent -> 0, StyleMenuListing -> None, 
                GridBoxOptions -> {
                 GridBoxAlignment -> {
                   "Columns" -> {{Left}}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {{Baseline}}, "RowsIndexed" -> {}}, 
                  GridBoxItemSize -> {"Columns" -> {{
                    Scaled[0.49]}}, "ColumnsIndexed" -> {}, "Rows" -> {{1.}}, 
                    "RowsIndexed" -> {}}}], 
               Cell[
                StyleData["2ColumnEvenTable", "Presentation"], FontSize -> 
                18], 
               Cell[
                StyleData["2ColumnEvenTable", "Printout"], 
                CellMargins -> {{2, 0}, {0, 8}}, FontSize -> 9]}, Closed]], 
            Cell[
             CellGroupData[{
               Cell[
                StyleData["3ColumnTable"], CellMargins -> {{35, 4}, {0, 8}}, 
                CellHorizontalScrolling -> True, LineIndent -> 0, 
                StyleMenuListing -> None, 
                GridBoxOptions -> {
                 GridBoxAlignment -> {
                   "Columns" -> {{Left}}, "ColumnsIndexed" -> {}, 
                    "Rows" -> {{Baseline}}, "RowsIndexed" -> {}}, 
                  GridBoxItemSize -> {"Columns" -> {
                    Scaled[0.28], 
                    Scaled[0.28], {
                    Scaled[0.43]}}, "ColumnsIndexed" -> {}, "Rows" -> {{1.}}, 
                    "RowsIndexed" -> {}}}], 
               Cell[
                StyleData["3ColumnTable", "Presentation"], FontSize -> 18], 
               Cell[
                StyleData["3ColumnTable", "Printout"], 
                CellMargins -> {{2, 0}, {0, 8}}, FontSize -> 9]}, Closed]]}, 
           Closed]]}, Closed]]}, Open]]}, Visible -> False, FrontEndVersion -> 
  "9.0 for Microsoft Windows (32-bit) (January 25, 2013)", StyleDefinitions -> 
  "Default.nb"]
]
(* End of Notebook Content *)

(* Internal cache information *)
(*CellTagsOutline
CellTagsIndex->{}
*)
(*CellTagsIndex
CellTagsIndex->{}
*)
(*NotebookFileOutline
Notebook[{
Cell[CellGroupData[{
Cell[1485, 35, 118, 3, 65, "Subtitle",
 Evaluatable->False],
Cell[1606, 40, 197, 6, 63, "Text",
 Evaluatable->False],
Cell[1806, 48, 484, 31, 32, "Message",
 Evaluatable->False],
Cell[2293, 81, 271, 8, 49, "Input"],
Cell[2567, 91, 246, 7, 28, "Input"],
Cell[2816, 100, 54, 1, 28, "Input"]
}, Open  ]],
Cell[2885, 104, 132, 3, 65, "Subtitle",
 Evaluatable->False],
Cell[CellGroupData[{
Cell[3042, 111, 111, 2, 97, "Title"],
Cell[3156, 115, 69, 1, 28, "Input"],
Cell[CellGroupData[{
Cell[3250, 120, 105, 2, 65, "Subtitle"],
Cell[3358, 124, 2790, 68, 229, "Input"],
Cell[CellGroupData[{
Cell[6173, 196, 94, 1, 80, "Section"],
Cell[6270, 199, 10569, 261, 769, "Input"]
}, Open  ]],
Cell[CellGroupData[{
Cell[16876, 465, 97, 1, 74, "Section"],
Cell[16976, 468, 12344, 332, 771, "Input"]
}, Open  ]],
Cell[CellGroupData[{
Cell[29357, 805, 92, 1, 74, "Section"],
Cell[29452, 808, 1866, 53, 109, "Input"]
}, Open  ]],
Cell[CellGroupData[{
Cell[31355, 866, 92, 1, 74, "Section"],
Cell[31450, 869, 2019, 58, 109, "Input"]
}, Open  ]],
Cell[CellGroupData[{
Cell[33506, 932, 94, 1, 74, "Section"],
Cell[33603, 935, 2356, 67, 129, "Input"]
}, Open  ]],
Cell[CellGroupData[{
Cell[35996, 1007, 91, 1, 74, "Section"],
Cell[36090, 1010, 11298, 303, 894, "Input"]
}, Open  ]],
Cell[CellGroupData[{
Cell[47425, 1318, 113, 2, 74, "Section"],
Cell[47541, 1322, 9463, 237, 928, "Input"],
Cell[CellGroupData[{
Cell[57029, 1563, 257, 8, 28, "Input"],
Cell[57289, 1573, 184, 4, 27, "Output"]
}, Open  ]],
Cell[CellGroupData[{
Cell[57510, 1582, 229, 8, 28, "Input"],
Cell[57742, 1592, 138, 4, 27, "Output"]
}, Open  ]]
}, Open  ]],
Cell[CellGroupData[{
Cell[57929, 1602, 178, 3, 74, "Section"],
Cell[58110, 1607, 13546, 304, 1051, "Input"]
}, Open  ]]
}, Open  ]]
}, Closed]],
Cell[CellGroupData[{
Cell[71717, 1918, 96, 2, 73, "Title"],
Cell[71816, 1922, 69, 1, 28, "Input"]
}, Closed]],
Cell[CellGroupData[{
Cell[71922, 1928, 193, 4, 71, "Title"],
Cell[72118, 1934, 177, 4, 28, "Input"],
Cell[72298, 1940, 369, 9, 28, "Input"],
Cell[CellGroupData[{
Cell[72692, 1953, 1787, 45, 89, "Input"],
Cell[74482, 2000, 19317, 323, 259, "Output"]
}, Open  ]]
}, Closed]],
Cell[CellGroupData[{
Cell[93848, 2329, 165, 3, 71, "Title"],
Cell[94016, 2334, 201, 4, 28, "Input"],
Cell[94220, 2340, 393, 9, 28, "Input"],
Cell[CellGroupData[{
Cell[94638, 2353, 3055, 82, 149, "Input"],
Cell[97696, 2437, 21050, 353, 159, "Output"]
}, Open  ]],
Cell[118761, 2793, 5959, 190, 538, "Input"],
Cell[CellGroupData[{
Cell[124745, 2987, 98, 1, 28, "Input"],
Cell[124846, 2990, 606, 12, 52, "Output"]
}, Open  ]],
Cell[CellGroupData[{
Cell[125489, 3007, 196, 3, 28, "Input"],
Cell[125688, 3012, 243, 5, 27, "Output"]
}, Open  ]],
Cell[125946, 3020, 181, 4, 28, "Input"],
Cell[126130, 3026, 181, 4, 28, "Input"],
Cell[126314, 3032, 225, 4, 28, "Input"],
Cell[126542, 3038, 224, 4, 28, "Input"],
Cell[CellGroupData[{
Cell[126791, 3046, 126, 2, 28, "Input"],
Cell[126920, 3050, 113, 1, 27, "Output"]
}, Open  ]],
Cell[127048, 3054, 85, 1, 28, "Input"],
Cell[CellGroupData[{
Cell[127158, 3059, 121, 2, 28, "Input"],
Cell[127282, 3063, 89, 1, 27, "Output"]
}, Open  ]],
Cell[127386, 3067, 87, 1, 28, "Input"]
}, Closed]],
Cell[CellGroupData[{
Cell[127510, 3073, 267, 5, 71, "Title"],
Cell[CellGroupData[{
Cell[127802, 3082, 4074, 112, 329, "Input"],
Cell[131879, 3196, 19252, 321, 363, "Output"]
}, Open  ]]
}, Open  ]]
}
]
*)

(* End of internal cache information *)

(* NotebookSignature IupoTa3jD@Zt8DKG3hp@PCf9 *)
