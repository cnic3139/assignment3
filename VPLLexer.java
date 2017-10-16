// Generated from VPL.g by ANTLR 4.7
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class VPLLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, FUNC=13, END=14, VAR=15, IF=16, WHILE=17, 
		THEN=18, DO=19, ENDIF=20, ENDWHILE=21, IDENT=22, NUM=23;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
		"T__9", "T__10", "T__11", "FUNC", "END", "VAR", "IF", "WHILE", "THEN", 
		"DO", "ENDIF", "ENDWHILE", "IDENT", "NUM"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'('", "')'", "','", "';'", "'='", "'add'", "'minus'", "'mult'", 
		"'div'", "'min'", "'<'", "'>'", "'func'", "'end'", "'var'", "'if'", null, 
		"'then'", "'do'", null, "'endwhile'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, "FUNC", "END", "VAR", "IF", "WHILE", "THEN", "DO", "ENDIF", "ENDWHILE", 
		"IDENT", "NUM"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public VPLLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "VPL.g"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\31\u0097\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\3\2"+
		"\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3"+
		"\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f"+
		"\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3"+
		"\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3"+
		"\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3"+
		"\26\3\26\3\26\3\26\3\26\3\27\3\27\7\27\u0086\n\27\f\27\16\27\u0089\13"+
		"\27\3\30\6\30\u008c\n\30\r\30\16\30\u008d\3\30\3\30\6\30\u0092\n\30\r"+
		"\30\16\30\u0093\5\30\u0096\n\30\2\2\31\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21"+
		"\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30"+
		"/\31\3\2\4\5\2C\\aac|\6\2\62;C\\aac|\2\u009a\2\3\3\2\2\2\2\5\3\2\2\2\2"+
		"\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2"+
		"\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2"+
		"\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2"+
		"\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\3\61\3\2\2\2\5\63\3\2\2"+
		"\2\7\65\3\2\2\2\t\67\3\2\2\2\139\3\2\2\2\r;\3\2\2\2\17?\3\2\2\2\21E\3"+
		"\2\2\2\23J\3\2\2\2\25N\3\2\2\2\27R\3\2\2\2\31T\3\2\2\2\33V\3\2\2\2\35"+
		"[\3\2\2\2\37_\3\2\2\2!c\3\2\2\2#f\3\2\2\2%l\3\2\2\2\'q\3\2\2\2)t\3\2\2"+
		"\2+z\3\2\2\2-\u0083\3\2\2\2/\u008b\3\2\2\2\61\62\7*\2\2\62\4\3\2\2\2\63"+
		"\64\7+\2\2\64\6\3\2\2\2\65\66\7.\2\2\66\b\3\2\2\2\678\7=\2\28\n\3\2\2"+
		"\29:\7?\2\2:\f\3\2\2\2;<\7c\2\2<=\7f\2\2=>\7f\2\2>\16\3\2\2\2?@\7o\2\2"+
		"@A\7k\2\2AB\7p\2\2BC\7w\2\2CD\7u\2\2D\20\3\2\2\2EF\7o\2\2FG\7w\2\2GH\7"+
		"n\2\2HI\7v\2\2I\22\3\2\2\2JK\7f\2\2KL\7k\2\2LM\7x\2\2M\24\3\2\2\2NO\7"+
		"o\2\2OP\7k\2\2PQ\7p\2\2Q\26\3\2\2\2RS\7>\2\2S\30\3\2\2\2TU\7@\2\2U\32"+
		"\3\2\2\2VW\7h\2\2WX\7w\2\2XY\7p\2\2YZ\7e\2\2Z\34\3\2\2\2[\\\7g\2\2\\]"+
		"\7p\2\2]^\7f\2\2^\36\3\2\2\2_`\7x\2\2`a\7c\2\2ab\7t\2\2b \3\2\2\2cd\7"+
		"k\2\2de\7h\2\2e\"\3\2\2\2fg\7y\2\2gh\7j\2\2hi\7k\2\2ij\7n\2\2jk\7g\2\2"+
		"k$\3\2\2\2lm\7v\2\2mn\7j\2\2no\7g\2\2op\7p\2\2p&\3\2\2\2qr\7f\2\2rs\7"+
		"q\2\2s(\3\2\2\2tu\7y\2\2uv\7j\2\2vw\7k\2\2wx\7n\2\2xy\7g\2\2y*\3\2\2\2"+
		"z{\7g\2\2{|\7p\2\2|}\7f\2\2}~\7y\2\2~\177\7j\2\2\177\u0080\7k\2\2\u0080"+
		"\u0081\7n\2\2\u0081\u0082\7g\2\2\u0082,\3\2\2\2\u0083\u0087\t\2\2\2\u0084"+
		"\u0086\t\3\2\2\u0085\u0084\3\2\2\2\u0086\u0089\3\2\2\2\u0087\u0085\3\2"+
		"\2\2\u0087\u0088\3\2\2\2\u0088.\3\2\2\2\u0089\u0087\3\2\2\2\u008a\u008c"+
		"\4\62;\2\u008b\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008b\3\2\2\2\u008d"+
		"\u008e\3\2\2\2\u008e\u0095\3\2\2\2\u008f\u0091\7\60\2\2\u0090\u0092\4"+
		"\62;\2\u0091\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0091\3\2\2\2\u0093"+
		"\u0094\3\2\2\2\u0094\u0096\3\2\2\2\u0095\u008f\3\2\2\2\u0095\u0096\3\2"+
		"\2\2\u0096\60\3\2\2\2\7\2\u0087\u008d\u0093\u0095\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}