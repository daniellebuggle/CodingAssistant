import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class VowelCheckTest {

    @Test
    public void testLowerCaseVowels() {
        assertTrue(VowelCheck.isVowel('a'));
        assertTrue(VowelCheck.isVowel('e'));
        assertTrue(VowelCheck.isVowel('i'));
        assertTrue(VowelCheck.isVowel('o'));
        assertTrue(VowelCheck.isVowel('u'));
    }

    @Test
    public void testUpperCaseVowels() {
        assertTrue(VowelCheck.isVowel('A'));
        assertTrue(VowelCheck.isVowel('E'));
        assertTrue(VowelCheck.isVowel('I'));
        assertTrue(VowelCheck.isVowel('O'));
        assertTrue(VowelCheck.isVowel('U'));
    }

    @Test
    public void testConsonants() {
        assertFalse(VowelCheck.isVowel('b'));
        assertFalse(VowelCheck.isVowel('c'));
        assertFalse(VowelCheck.isVowel('d'));
        assertFalse(VowelCheck.isVowel('z'));
        assertFalse(VowelCheck.isVowel('X'));
    }

    @Test
    public void testNonAlphabetCharacters() {
        assertFalse(VowelCheck.isVowel('1'));
        assertFalse(VowelCheck.isVowel('$'));
        assertFalse(VowelCheck.isVowel('#'));
        assertFalse(VowelCheck.isVowel(' ')); // Space
    }

    @Test
    public void testEmptyChar() {
        assertFalse(VowelCheck.isVowel('\0')); // Null character
    }
}
