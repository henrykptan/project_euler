import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

/**
 * Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information
 * Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
 * <p>
 * A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret
 * key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example,
 * 65 XOR 42 = 107, then 107 XOR 42 = 65.
 * <p>
 * For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would
 * keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the
 * message.
 * <p>
 * Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is
 * shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a
 * sufficiently long password key for security, but short enough to be memorable.
 * <p>
 * Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt (right click and 'Save
 * Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English
 * words, decrypt the message and find the sum of the ASCII values in the original text.
 * <p>
 * <p>
 * Ideas: Password has to be lower case letters ie. 97 - 122
 * <p>
 * Assume that English can't have ascii 0 - 31?
 */


public class P59 {

    public static List<Integer> decryptFile(List<Integer> asciiNums, List<String> passwordLetters) {
        List<Integer> passwordNums = passwordLetters.stream().map(P59::getAsciiCodeFromChar).collect(Collectors.toList());
        List<Integer> decryptedNums = new ArrayList<>();
        for (int index = 0; index < asciiNums.size(); index++) {
            decryptedNums.add(P59.decrypt(asciiNums.get(index), passwordNums.get(index % 3)));
        }
        return decryptedNums;
    }

    public static int decrypt(int asciiNum, int passwordNum) {
        return asciiNum ^ passwordNum;
    }

    private static String getCharFromAsciiCode(int asciiCode) {
        return Character.toString((char) asciiCode);
    }

    private static int getAsciiCodeFromChar(String c) {
        return c.charAt(0);
    }

    private static boolean isValidAscii(int ascii) {
        return ((31 < ascii) && (ascii < 94)) || ((96 < ascii) && (ascii < 123));
    }

    private static List<Integer> getCipherNums() throws IOException {
        ClassLoader classloader = Thread.currentThread().getContextClassLoader();
        try (BufferedReader cipherReader = new BufferedReader(
                new InputStreamReader(Objects.requireNonNull(classloader.getResourceAsStream(("p059_cipher.txt")))))) {
            return cipherReader.lines().flatMap(line -> Stream.of(line.split(",")))
                               .map(Integer::parseInt)
                               .collect(Collectors.toList());
        }

    }


    public static void main(String[] args) throws IOException {

        HashMap<Integer, List<Integer>> possiblePasswordNumAtEachIndex = new HashMap<>();

        for (int startIndex = 0; startIndex < 3; startIndex++) {
            possiblePasswordNumAtEachIndex.put(startIndex, new ArrayList<>());
            List<Integer> cipherNums = P59.getCipherNums();

            int finalStartIndex = startIndex;
            List<Integer> numsToConsider = IntStream.range(0, cipherNums.size())
                                                    .filter(n -> (n - finalStartIndex) % 3 == 0)
                                                    .mapToObj(cipherNums::get)
                                                    .collect(Collectors.toList());

            for (int possiblePasswordNum = 97; possiblePasswordNum < 123; possiblePasswordNum++) {
                int finalPossiblePasswordNum = possiblePasswordNum;
                if (numsToConsider.stream().map(num -> P59.decrypt(num, finalPossiblePasswordNum))
                                  .allMatch(P59::isValidAscii))
                    possiblePasswordNumAtEachIndex.get(startIndex).add(possiblePasswordNum);
            }

        }

        if (possiblePasswordNumAtEachIndex.get(0).size() != 1 &&
            possiblePasswordNumAtEachIndex.get(1).size() != 1 &&
            possiblePasswordNumAtEachIndex.get(2).size() != 1) {
            System.out.println("Not good enough");

        } else {
            List<String> letterPassword = possiblePasswordNumAtEachIndex.values().stream()
                                                                        .flatMap(l -> Stream.of(l.get(0)))
                                                                        .map(P59::getCharFromAsciiCode)
                                                                        .collect(Collectors.toList());
            List<Integer> decryptedAscii = decryptFile(P59.getCipherNums(), letterPassword);
            System.out.printf("Password is: %s%n \n", letterPassword);
            System.out.printf("Text is: %s \n", decryptedAscii.stream().map(P59::getCharFromAsciiCode)
                                                           .collect(Collectors.joining()));
            System.out.printf("Ascii sum is: %s", decryptedAscii.stream().mapToInt(Integer::intValue).sum());
        }


    }
}

