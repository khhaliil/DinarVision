import cv2
import pyttsx3
import parameters as params
import functions as funcs

def main():
    # Initialize the speech engine
    engine = pyttsx3.init()
    engine.setProperty("rate", params.RATE)
    engine.setProperty('voice', params.LANG)

    # Initialize video capture
    cap = cv2.VideoCapture(params.CAMERA_DEVICE_ID)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, params.FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, params.FRAME_HEIGHT)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Get the sum from the AI model
        sum_value = funcs.get_sum_from_camera(frame)

        # Speak the sum
        funcs.speak_sum(sum_value, engine)

        # Display the sum on the frame
        cv2.putText(frame, f'Sum: {sum_value}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('Frame', frame)

        # If there is an upload demand, upload the file to Google Drive
        if funcs.upload_demand():
            funcs.upload_to_gdrive(params.SEND_LOCAL_PATH, params.SEND_REMOTE_PATH, params.RCLONE_CONFIG_NAME)

        # If there is an update demand, download the file from Google Drive
        if funcs.update_demand():
            funcs.download_from_gdrive(params.RECEIVE_LOCAL_PATH, params.RECEIVE_REMOTE_PATH, params.RCLONE_CONFIG_NAME)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()

# Execute the main function
if __name__ == '__main__':
    main()
