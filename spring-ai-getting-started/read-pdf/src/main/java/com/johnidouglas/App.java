package com.johnidouglas;

import org.apache.pdfbox.Loader;

import org.apache.pdfbox.io.RandomAccessReadBufferedFile;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.text.PDFTextStripper;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

public class App {

    public static void main(String[] args) {

        String filename = "/home/johni.marangon@softplan.com.br/Projects/udemy-course-code-repository/spring-ai-getting-started/read-pdf/example.pdf";

        readPDFFileByApachePDFBox(filename);

    }

    private static void readPDFFileByApachePDFBox(String filePath) {
        try (PDDocument document = Loader.loadPDF(new RandomAccessReadBufferedFile(filePath))) {
            if (!document.isEncrypted()) {
                PDFTextStripper pdfStripper = new PDFTextStripper();
                String text = pdfStripper.getText(document);
                System.out.println(text);
            } else {
                System.out.println("The document is encrypted and cannot be read.");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
