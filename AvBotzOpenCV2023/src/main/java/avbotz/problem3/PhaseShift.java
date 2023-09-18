package avbotz.problem3;

import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.ArrayList;
import java.util.Scanner; // Import the Scanner class to read text files

public class PhaseShift {
    public static void main(String[] args) {
        String fileName = "/Users/Rishit/IdeaProjects/TestOpenCV/src/main/java/avbotz/problem3/signalAAA.txt";

        ArrayList<Double> functionCoordinates = readFile(fileName);
        System.out.println(functionCoordinates);

        makeSinusoidalFunction(functionCoordinates);
    }

    public static ArrayList<Double> readFile(String file) {
        ArrayList<ArrayList<Double>> functionCoordinates = new ArrayList<>();
        ArrayList<Double> coordinate = new ArrayList<>();

        try {
            File myObj = new File(file);
            Scanner myReader = new Scanner(myObj);

            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                coordinate.add(Double. parseDouble(data));

            }

            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred while trying to read file");
            e.printStackTrace();
        }

        return coordinate;
    }

    private static void makeSinusoidalFunction(ArrayList<Double> coords){
        for (int i = 0; i < coords.size(); i++) {

        }
    }
}
