package avbotz.problem1;

import nu.pattern.OpenCV;
import org.opencv.calib3d.Calib3d;
import org.opencv.core.*;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;
import org.opencv.highgui.HighGui;

import java.util.ArrayList;
import java.util.Random;

/**
 * Uses later in the program to efficiently stores coordinates
 */
class Coordinate {
    private int x;
    private int y;

    public Coordinate(int x, int y) {
        this.x = x;
        this.y = y;
    }
    public int getY() {
        return y;
    }

    public int getX() {
        return x;
    }

    @Override
    public String toString() {
        return "avbotz.problem1.Coordinate{" +
                "x=" + x +
                ", y=" + y +
                '}';
    }
}

public class TorpBoard {
    public static void main(String[] args) {
        OpenCV.loadShared();

        //Load the OpenCv Core library
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
        //File name for the image. Replace name with different files
        String fileName = "/Users/Rishit/IdeaProjects/TestOpenCV/src/main/resources/torpBoard2.png";

        //The source image and the gray scaled image
        final Mat sourceImg = readImg(fileName);
        final Mat grayScaledImage = grayScaleImg(sourceImg);

        //Function to detect corners of image
        ArrayList<Coordinate> imgCoordinatesList= detectImgCoordinates(sourceImg, grayScaledImage);
        System.out.println(imgCoordinatesList);

        //Method find corner coordinates of the image
        int[][] cornerCoords = findCornerCoords(imgCoordinatesList);

        //Calculates the center using corner coordinates
        Coordinate centerCoord = findCenterCoord(cornerCoords);
        System.out.println("Center coordinate = " + centerCoord);

        //Uncomment this method to shoe an image of detected coordinates on the torp board
        //copyDetectCorners(sourceImg, grayScaledImage);

        //Method to detect orient angle
       findOrientAngle(cornerCoords, centerCoord);

    }

    /**
     * Return a matrix with the contents of the source image
     * @param file
     * @return
     */
    private static Mat readImg(String file) {
        //Instantiating the Imagecodecs class
        Imgcodecs imageCodecs = new Imgcodecs();

        Mat src = imageCodecs.imread(file);

        //double width = src.size().width;
        //double height = src.size().height;
        //System.out.println(width + " " + height);


        //Reading the Image from the file
        return src;
    }

    /**
     * Converts RGB image to a grayscaled image
     * @param srcImg
     * @return
     */
    private static Mat grayScaleImg(Mat srcImg) {
        //Create a copy of the source image
        Mat copySrc = srcImg.clone();

        // Creating the empty destination matrix
        Mat destination = new Mat();

        // Converting the image to grayscale and saving it in the destination matrix
        Imgproc.cvtColor(copySrc, destination, Imgproc.COLOR_RGB2GRAY);

        return destination;
    }

    /**
     * Displays the image on a window
     * @param img
     */
    private static void displayImg(Mat img) {
        HighGui.imshow("Image", img);
        HighGui.waitKey();
    }


    /**
     * Detects corners of the torp board using Imgproc
     * @param srcImg
     * @param grayImg
     * @return
     */
    private static ArrayList<Coordinate> detectImgCoordinates(Mat srcImg, Mat grayImg) {
        //Creates empty list of matrix points
        MatOfPoint corners = new MatOfPoint();
        //Identifies the number of corners, quality of corners, and minimum distance between corners
        //20 corners taken to ensure all the corners have been selected
        int maxCorners = 20;
        double qualityLevel = 0.01;
        double minDistance = 10;

        //Good features to track method determines strong corners on an image
        Imgproc.goodFeaturesToTrack(grayImg, corners, maxCorners, qualityLevel, minDistance);
        System.out.println("** Number of corners detected: " + corners.rows());

        //Calculates the coordinate data of the corners detected and puts them into an integer array
        int[] cornersData = new int[(int) (corners.total() * corners.channels())];
        corners.get(0, 0, cornersData);


        //Organize the coordinate data into a ArrayList of objects that each contain
        //the x and y values for each coordinate
        ArrayList<Coordinate> coordinateList = new ArrayList<>();
        for (int i = 0; i < 20; i++) {
            Coordinate objCoordinate = new Coordinate(cornersData[i * 2], cornersData[i * 2 + 1]);
            coordinateList.add(objCoordinate);
        }

        return coordinateList;

    }

    /**
     * Determines the four coordinates of the corners of the torp board
     * @param imgCoordinatesList
     * @return
     */
    private static int[][] findCornerCoords(ArrayList<Coordinate> imgCoordinatesList) {
        //These four values determine the corner coords of the torp board in any image
        Coordinate maxXCoordinate = imgCoordinatesList.get(0);
        Coordinate minXCoordinate = imgCoordinatesList.get(0);

        Coordinate maxYCoordinate = imgCoordinatesList.get(0);
        Coordinate minYCoordinate = imgCoordinatesList.get(0);

        //Check for maxX, minX, maxY, minY in all the corrdinates
        for (int i = 1; i < imgCoordinatesList.size(); i++) {
            Coordinate objCoordinate = imgCoordinatesList.get(i);
            int xCoord = objCoordinate.getX();
            int yCoord = objCoordinate.getY();


            if(xCoord > maxXCoordinate.getX()) {
                maxXCoordinate = objCoordinate;
            } else if (xCoord < minXCoordinate.getX()) {
                minXCoordinate = objCoordinate;
            }

            if(yCoord > maxYCoordinate.getY()) {
                maxYCoordinate = objCoordinate;
            } else if (yCoord < minYCoordinate.getY()) {
                minYCoordinate = objCoordinate;
            }
        }
        //Stores and returns x and y coordinate pairs
        int[] maxX = { maxXCoordinate.getX(),maxXCoordinate.getY() };
        int[] minX = { minXCoordinate.getX(),minXCoordinate.getY() };
        int[] maxY = { maxYCoordinate.getX(),maxYCoordinate.getY() };
        int[] minY = { minYCoordinate.getX(),minYCoordinate.getY() };

        int[][] cornerCoords = {maxX, minX, maxY, minY};

        return cornerCoords;
    }

    /**
     * Uses corner coordinate to find center coordinate. Very accurate!
     * @param cornerCoords
     * @return
     */
    private static Coordinate findCenterCoord(int[][] cornerCoords) {
        //Formula to find the center coordinate of a quadrilateral
        //Two points: (A,B) (C,D)
        //(A+C)/2, (B+D)/2
        int centerXCoord = (cornerCoords[0][0] + cornerCoords[1][0]) / 2;
        int centerYCoord = (cornerCoords[2][1] + cornerCoords[3][1]) / 2;

        return new Coordinate(centerXCoord, centerYCoord);
    }

    //Find orient angle
    //Unable to solve yet
    private static void findOrientAngle(int[][] cornerCoords, Coordinate centerCoord) {
        // Define the 2D points of the rectangle and its center
        Point[] rectanglePoints = new Point[4];

        // Fill in the coordinates of the rectangle's corners (clockwise or counterclockwise)

        rectanglePoints[0] = new Point(cornerCoords[2][0],cornerCoords[2][1]); // Top-left
        rectanglePoints[1] = new Point(cornerCoords[0][0],cornerCoords[0][1]); // Top-right
        rectanglePoints[2] = new Point(cornerCoords[3][0],cornerCoords[3][1]); // Bottom-right
        rectanglePoints[3] = new Point(cornerCoords[1][0],cornerCoords[1][1]); // Bottom-left

        Point center = new Point(centerCoord.getX(), centerCoord.getY());

        // Define the 3D coordinates of the rectangle in its local coordinate system
        // Assuming that the rectangle lies flat on the XY plane
        double rectZ = 0.0; // Assuming it's at z = 0

        MatOfPoint3f objectPoints = new MatOfPoint3f();
        for (int i = 0; i < 4; i++) {
            objectPoints.push_back(new MatOfPoint3f(new Point3(rectanglePoints[i].x - center.x, rectanglePoints[i].y - center.y, rectZ)));
        }

        // Define camera matrix and distortion coefficients (you may need to calibrate your camera)
        Mat cameraMatrix = new Mat(3, 3, CvType.CV_64F);

        // Fill in your camera matrix values
        // Trouble finding focal c and y
        cameraMatrix.put(70, 0, center.x);
        cameraMatrix.put(0, 70, center.y);
        cameraMatrix.put(0, 0, 1);


        MatOfDouble distCoeffs = new MatOfDouble();
        // Fill in your distortion coefficients if applicable

        // Output rotation and translation vectors
        Mat rvec = new Mat();
        Mat tvec = new Mat();

        // Perform solvePnP to find the pose of the rectangle
        Calib3d.solvePnP(objectPoints, new MatOfPoint2f(rectanglePoints), cameraMatrix, distCoeffs, rvec, tvec);

        // Convert rotation vector to rotation matrix
        Mat rotationMatrix = new Mat(3, 3, CvType.CV_64F);
        Calib3d.Rodrigues(rvec, rotationMatrix);


        //Calculate orientation angle
        //Not sure if this is the correct formula
        double relativeOrientationAngle = Math.atan2(rotationMatrix.get(1, 0)[0], rotationMatrix.get(0, 0)[0]);
        relativeOrientationAngle = Math.toDegrees(relativeOrientationAngle);

        System.out.println("Orientation Angle: " + relativeOrientationAngle);
    }

    /**
     * Run this function to see each image with detected coordinates
     * @param srcImg
     * @param grayImg
     */
    private static void copyDetectCorners(Mat srcImg, Mat grayImg) {
        MatOfPoint corners = new MatOfPoint();
        int maxCorners = 20;
        double qualityLevel = 0.01;
        double minDistance = 10;

        Mat copy = srcImg.clone();
        Random rng = new Random(12345);

        //Good features to track method determines strong corners on an image
        Imgproc.goodFeaturesToTrack(grayImg, corners, maxCorners, qualityLevel, minDistance);

        System.out.println("Number of corners detected: " + corners.rows());

        int[] cornersData = new int[(int) (corners.total() * corners.channels())];
        corners.get(0, 0, cornersData);


        int radius = 4;
        Mat matCorners = new Mat(corners.rows(), 2, CvType.CV_32F);

        float[] matCornersData = new float[(int) (matCorners.total() * matCorners.channels())];
        matCorners.get(0, 0, matCornersData);


        for (int i = 0; i < corners.rows(); i++) {
            Imgproc.circle(copy, new Point(cornersData[i * 2], cornersData[i * 2 + 1]), radius,
                    new Scalar(rng.nextInt(256), rng.nextInt(256), rng.nextInt(256)), Core.FILLED);
            matCornersData[i * 2] = cornersData[i * 2];
            matCornersData[i * 2 + 1] = cornersData[i * 2 + 1];
        }

        matCorners.put(0, 0, matCornersData);

        Size winSize = new Size(5, 5);
        Size zeroZone = new Size(-1, -1);
        TermCriteria criteria = new TermCriteria(TermCriteria.EPS + TermCriteria.COUNT, 40, 0.001);


        Imgproc.cornerSubPix(grayImg, matCorners, winSize, zeroZone, criteria);


        matCorners.get(0, 0, matCornersData);


        for (int i = 0; i < corners.rows(); i++) {
            System.out.println(
                    "Corner: [" + i + "] (" + matCornersData[i * 2] + "," + matCornersData[i * 2 + 1] + ")");
        }

        displayImg(copy);
    }
}
